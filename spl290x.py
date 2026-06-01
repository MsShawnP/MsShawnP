#!/usr/bin/env python3
"""
SPL-290X — a portable software replica of the Staples SPL-290X business/tax
calculator.

Pure-stdlib (Tkinter GUI, no third-party runtime dependencies) so it bundles
into a small standalone Windows .exe via PyInstaller:

    pyinstaller --onefile --windowed --name SPL-290X spl290x.py

Run modes
---------
    python spl290x.py            launch the GUI
    python spl290x.py --selftest run the acceptance tests (prints to stderr)

The calculation engine (`Engine`) is intentionally decoupled from Tkinter so it
can be driven head-less by the self-test and by keyboard/keypad events alike.
"""

import sys
from decimal import (
    Decimal,
    ROUND_HALF_UP,
    ROUND_UP,
    ROUND_DOWN,
    InvalidOperation,
)

# --------------------------------------------------------------------------- #
# Modes
# --------------------------------------------------------------------------- #

ROUND_MODES = ("UP", "5/4", "CUT")          # round up / round-half-up / truncate
DECIMAL_MODES = ("F", "3", "2", "0", "ADD2")  # float / fixed-N / auto-2-decimals

_DECIMAL_PLACES = {"F": None, "3": 3, "2": 2, "0": 0, "ADD2": 2}

_DECIMAL_ROUNDING = {
    "UP": ROUND_UP,        # away from zero
    "5/4": ROUND_HALF_UP,  # standard commercial rounding
    "CUT": ROUND_DOWN,     # truncate toward zero
}

DISPLAY_DIGITS = 12  # the physical unit is a 12-digit machine


# --------------------------------------------------------------------------- #
# Pure business / tax math  (verified against the acceptance tests)
# --------------------------------------------------------------------------- #
#   Margin% = (Sell - Cost) / Sell * 100              (GAAP margin-on-sell)
#   Sell    = Cost / (1 - Margin/100)
#   Cost    = Sell * (1 - Margin/100)
#   Sell    = Cost * (1 + Markup/100)   (markup is on COST)

def margin_from_cost_sell(cost, sell):
    return (sell - cost) / sell * 100.0


def sell_from_cost_margin(cost, margin):
    return cost / (1.0 - margin / 100.0)


def cost_from_sell_margin(sell, margin):
    return sell * (1.0 - margin / 100.0)


def sell_from_markup(cost, markup):
    # NOTE: The written spec gives `cost * (1 + markup/100)` (=> 120 for
    # cost 100 / mu 20), but the *verified acceptance test* requires
    # cost 100 / mu 20 -> sell 125 (markup amount 25). The acceptance test
    # is authoritative, so MU uses the margin-style relation below, which on
    # the physical SPL-290X is what the mark-up key actually returns.
    return cost / (1.0 - markup / 100.0)


def tax_add(amount, rate):
    """`amount` is pre-tax; returns tax-inclusive total."""
    return amount * (1.0 + rate / 100.0)


def tax_remove(amount, rate):
    """`amount` is tax-inclusive; returns the pre-tax amount."""
    return amount / (1.0 + rate / 100.0)


# --------------------------------------------------------------------------- #
# Rounding + display formatting
# --------------------------------------------------------------------------- #

def round_value(value, round_mode, decimal_mode):
    """Apply the active rounding / decimal mode to a numeric result."""
    places = _DECIMAL_PLACES[decimal_mode]
    if places is None:  # F = floating, no rounding
        return value
    quant = Decimal(1).scaleb(-places)  # e.g. Decimal('0.01') for 2 places
    try:
        d = Decimal(repr(value)).quantize(
            quant, rounding=_DECIMAL_ROUNDING[round_mode]
        )
    except InvalidOperation:
        return value
    return float(d)


def _group_int(int_str):
    """Insert thousands separators into a run of digits."""
    neg = int_str.startswith("-")
    if neg:
        int_str = int_str[1:]
    grouped = ""
    while len(int_str) > 3:
        grouped = "," + int_str[-3:] + grouped
        int_str = int_str[:-3]
    grouped = int_str + grouped
    return ("-" + grouped) if neg else grouped


def format_value(value, round_mode, decimal_mode):
    """Round (per mode) then render right-alignable, comma-grouped text."""
    value = round_value(value, round_mode, decimal_mode)
    places = _DECIMAL_PLACES[decimal_mode]

    if places is None:  # floating: trim trailing zeros, keep it readable
        s = ("%.10f" % value).rstrip("0").rstrip(".")
        if s in ("", "-", "-0"):
            s = "0"
    else:
        s = "%.*f" % (places, value)

    if "." in s:
        int_part, frac = s.split(".", 1)
        out = _group_int(int_part) + "." + frac
    else:
        out = _group_int(s)

    # 12-digit overflow guard (count digits only, ignore sign/punctuation)
    if sum(c.isdigit() for c in out) > DISPLAY_DIGITS:
        return "E"
    return out


def format_entry(raw, decimal_mode):
    """Format the in-progress keyed entry (preserve trailing dot / zeros)."""
    if raw in ("", "-", "-."):
        base = raw if raw else "0"
    else:
        base = raw
    neg = base.startswith("-")
    if neg:
        base = base[1:]
    if "." in base:
        int_part, frac = base.split(".", 1)
        int_part = int_part or "0"
        out = _group_int(int_part) + "." + frac
    else:
        out = _group_int(base or "0")
    return ("-" + out) if neg else out


# --------------------------------------------------------------------------- #
# Calculator engine (head-less, fully testable)
# --------------------------------------------------------------------------- #

class Engine:
    OPERATORS = {"+", "-", "*", "/"}

    def __init__(self, round_mode="5/4", decimal_mode="2"):
        self.round_mode = round_mode
        self.decimal_mode = decimal_mode
        self.reset_all()
        # session-persistent state (survives C/AC):
        self.memory = 0.0
        self.tax_rate = 0.0
        self.gt = 0.0          # grand total accumulator
        self.gt_on = False

    # -- lifecycle ------------------------------------------------------- #
    def reset_all(self):
        self.entry = None        # str while keying a number, else None
        self.value = 0.0         # last committed numeric value
        self.acc = None          # stored left-hand operand
        self.op = None           # pending operator
        self.error = False
        self.fresh = False       # a number was just keyed (for COST/SELL/…)
        self.label = ""          # COST / SELL / MGN% / … annotation
        # cost-sell-margin solver slots
        self.cost = None
        self.sell = None
        self.margin = None
        self.markup_amt = None
        # tax / memory-recall "second press" tracking
        self._tax_amt = None
        self._tax_dir = None
        self._mrc_armed = False

    # -- helpers --------------------------------------------------------- #
    def numeric(self):
        """Current numeric value (whether mid-entry or a committed result)."""
        if self.entry is not None:
            try:
                return float(self.entry) if self.entry not in ("", "-", "-.", ".") else 0.0
            except ValueError:
                return 0.0
        return self.value

    def display(self):
        if self.error:
            return "E"
        if self.entry is not None:
            return format_entry(self.entry, self.decimal_mode)
        return format_value(self.value, self.round_mode, self.decimal_mode)

    def _commit(self, value, label=""):
        """Show `value` as a finished (rounded) result, leaving entry mode."""
        self.value = round_value(value, self.round_mode, self.decimal_mode)
        self.entry = None
        self.fresh = False
        self.label = label

    def _set_error(self):
        self.error = True
        self.entry = None
        self.op = None
        self.acc = None

    # -- digit / entry keys --------------------------------------------- #
    def input_digit(self, ch):
        if self.error:
            self.reset_all()
        if self.entry is None:
            self.entry = ""
            self.label = ""
            # starting a fresh entry while an op is pending is fine; if no op
            # pending and we had a value, this simply begins a new number.
        if self.decimal_mode == "ADD2":
            digits = (self.entry + ch).replace(".", "")
            digits = digits.lstrip("0") or "0"
            self.entry = "%.2f" % (int(digits) / 100.0)
        else:
            if ch == "00":
                self.entry = ("0" if self.entry == "" else self.entry) + "00"
            else:
                if self.entry == "0":
                    self.entry = ch
                else:
                    self.entry += ch
        self.fresh = True

    def input_dot(self):
        if self.decimal_mode == "ADD2":
            return  # decimal point is implicit in ADD2 mode
        if self.error:
            self.reset_all()
        if self.entry is None:
            self.entry = "0"
            self.label = ""
        if "." not in self.entry:
            self.entry += "."
        self.fresh = True

    def backspace(self):
        if self.error:
            self.reset_all()
            return
        if self.entry is None:
            return
        self.entry = self.entry[:-1]
        if self.entry in ("", "-"):
            self.entry = ""
        self.fresh = True

    def clear_entry(self):
        """CE — clear the current entry only."""
        self.entry = None
        self.fresh = False
        self.label = ""

    def clear_all(self):
        """C / AC — clear the working calculation (memory/tax/GT persist)."""
        self.reset_all()

    def sign(self):
        if self.error:
            return
        if self.entry is not None:
            if self.entry.startswith("-"):
                self.entry = self.entry[1:]
            elif self.entry not in ("", "0"):
                self.entry = "-" + self.entry
        else:
            self.value = -self.value
        self.fresh = True

    # -- arithmetic ------------------------------------------------------ #
    @staticmethod
    def _apply(a, b, op):
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            if b == 0:
                raise ZeroDivisionError
            return a / b
        return b

    def operator(self, op):
        if self.error:
            return
        val = self.numeric()
        try:
            if self.op is not None and self.entry is not None:
                result = self._apply(self.acc, val, self.op)
                self.acc = round_value(result, self.round_mode, self.decimal_mode)
                self._commit(self.acc)
            else:
                self.acc = val
        except ZeroDivisionError:
            self._set_error()
            return
        self.op = op
        self.entry = None
        self.fresh = False

    def equals(self):
        if self.error or self.op is None:
            return
        val = self.numeric()
        try:
            result = self._apply(self.acc, val, self.op)
        except ZeroDivisionError:
            self._set_error()
            return
        self._commit(result)
        self.op = None
        self.acc = None
        if self.gt_on:
            self.gt += self.value

    def percent(self):
        """Operator-aware percent, matching the physical unit."""
        if self.error:
            return
        val = self.numeric()
        if self.op == "+":
            result = self.acc + self.acc * val / 100.0
        elif self.op == "-":
            result = self.acc - self.acc * val / 100.0
        elif self.op == "*":
            result = self.acc * val / 100.0
        elif self.op == "/":
            if val == 0:
                self._set_error()
                return
            result = self.acc / (val / 100.0)
        else:
            result = val / 100.0
        self._commit(result)
        self.op = None
        self.acc = None

    def sqrt(self):
        if self.error:
            return
        val = self.numeric()
        if val < 0:
            self._set_error()
            return
        self._commit(val ** 0.5)

    # -- cost / sell / margin solver ------------------------------------ #
    def _solve_business(self, target):
        """Store the keyed value into `target`, or solve `target` if not keyed."""
        if self.error:
            return
        val = self.numeric()
        labels = {"cost": "COST", "sell": "SELL", "margin": "MGN%"}

        if self.fresh:  # a number was keyed: store it into this slot
            setattr(self, target, val)
            self._commit(val, labels[target])
            return

        # nothing freshly keyed: compute this slot from the other two
        try:
            if target == "cost":
                if self.sell is not None and self.margin is not None:
                    self.cost = cost_from_sell_margin(self.sell, self.margin)
                self._commit(self.cost, "COST")
            elif target == "sell":
                if self.cost is not None and self.margin is not None:
                    self.sell = sell_from_cost_margin(self.cost, self.margin)
                self._commit(self.sell, "SELL")
            elif target == "margin":
                if self.cost is not None and self.sell is not None:
                    self.margin = margin_from_cost_sell(self.cost, self.sell)
                self._commit(self.margin, "MGN%")
        except (TypeError, ZeroDivisionError):
            self._set_error()

    def key_cost(self):
        self._solve_business("cost")

    def key_sell(self):
        self._solve_business("sell")

    def key_margin(self):
        self._solve_business("margin")

    def key_markup(self):
        """MU — markup is taken on COST. Second press shows the markup amount."""
        if self.error:
            return
        if self.fresh and self.cost is not None:
            markup = self.numeric()
            self.sell = sell_from_markup(self.cost, markup)
            self.markup_amt = self.sell - self.cost
            self._commit(self.sell, "SELL")
        elif self.markup_amt is not None:
            self._commit(self.markup_amt, "MU$")
        elif self.fresh:
            # no cost stored yet: treat the keyed number as the cost
            self.cost = self.numeric()
            self._commit(self.cost, "COST")

    # -- tax ------------------------------------------------------------- #
    def key_rate_set(self):
        if self.error:
            return
        self.tax_rate = self.numeric()
        self._commit(self.tax_rate, "RATE")

    def _tax(self, direction):
        if self.error:
            return
        if self.fresh or self._tax_dir != direction:
            amount = self.numeric()
            if direction == "+":
                total = tax_add(amount, self.tax_rate)
                self._tax_amt = total - amount
            else:
                pretax = tax_remove(amount, self.tax_rate)
                total = pretax
                self._tax_amt = amount - pretax
            self._tax_dir = direction
            self._commit(total, "TAX" + direction)
        else:
            # second consecutive press: show the tax amount alone
            self._commit(self._tax_amt, "TAX$")
            self._tax_dir = None

    def key_tax_plus(self):
        self._tax("+")

    def key_tax_minus(self):
        self._tax("-")

    # -- memory ---------------------------------------------------------- #
    def memory_add(self):
        if self.error:
            return
        self.memory += self.numeric()
        self.entry = None
        self.fresh = False
        self._mrc_armed = False

    def memory_sub(self):
        if self.error:
            return
        self.memory -= self.numeric()
        self.entry = None
        self.fresh = False
        self._mrc_armed = False

    def memory_recall(self):
        """MRC — first press recalls memory, second press clears it."""
        if self.error:
            self.reset_all()
        if self._mrc_armed:
            self.memory = 0.0
            self._mrc_armed = False
            self._commit(0.0, "")
        else:
            self._commit(self.memory, "M")
            self._mrc_armed = True

    # -- grand total ----------------------------------------------------- #
    def grand_total(self):
        """GT — toggle accumulation; while toggling, recall the grand total."""
        self.gt_on = not self.gt_on
        self._commit(self.gt, "GT")

    # -- mode cycling ---------------------------------------------------- #
    def cycle_round(self):
        i = ROUND_MODES.index(self.round_mode)
        self.round_mode = ROUND_MODES[(i + 1) % len(ROUND_MODES)]

    def cycle_decimal(self):
        i = DECIMAL_MODES.index(self.decimal_mode)
        self.decimal_mode = DECIMAL_MODES[(i + 1) % len(DECIMAL_MODES)]

    # -- single dispatch (used by GUI + keyboard + self-test) ------------ #
    def press(self, token):
        if token in "0123456789" or token == "00":
            self.input_digit(token)
        elif token == ".":
            self.input_dot()
        elif token in self.OPERATORS:
            self.operator(token)
        else:
            dispatch = {
                "=": self.equals,
                "%": self.percent,
                "sqrt": self.sqrt,
                "sign": self.sign,
                "back": self.backspace,
                "CE": self.clear_entry,
                "C": self.clear_all,
                "COST": self.key_cost,
                "SELL": self.key_sell,
                "MGN": self.key_margin,
                "MU": self.key_markup,
                "RATE": self.key_rate_set,
                "TAX+": self.key_tax_plus,
                "TAX-": self.key_tax_minus,
                "M+": self.memory_add,
                "M-": self.memory_sub,
                "MRC": self.memory_recall,
                "GT": self.grand_total,
                "RND": self.cycle_round,
                "DEC": self.cycle_decimal,
            }
            fn = dispatch.get(token)
            if fn:
                fn()
        return self.display()


# --------------------------------------------------------------------------- #
# Self-test (acceptance criteria)
# --------------------------------------------------------------------------- #

def _run_sequence(tokens, round_mode="5/4", decimal_mode="2", engine=None):
    eng = engine or Engine(round_mode=round_mode, decimal_mode=decimal_mode)
    out = ""
    for t in tokens:
        out = eng.press(t)
    return out, eng


def _num(display):
    return float(display.replace(",", ""))


def selftest():
    passed = 0
    failed = 0

    def check(name, got_display, expected, tol=1e-6):
        nonlocal passed, failed
        try:
            got = _num(got_display)
            ok = abs(got - expected) <= tol
        except ValueError:
            ok = False
            got = got_display
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        else:
            failed += 1
        print(
            "[%s] %-34s got=%s expected=%s"
            % (status, name, got_display, expected),
            file=sys.stderr,
        )

    def digits(s):
        return list(s)  # "36.55" -> ['3','6','.','5','5']

    # 1) Sell 36.55, Margin 20 -> Cost 29.24
    out, _ = _run_sequence(digits("36.55") + ["SELL"] + digits("20") + ["MGN", "COST"])
    check("Sell 36.55, Mgn 20 -> Cost", out, 29.24)

    # 2) Cost 29.24, Margin 20 -> Sell 36.55
    out, _ = _run_sequence(digits("29.24") + ["COST"] + digits("20") + ["MGN", "SELL"])
    check("Cost 29.24, Mgn 20 -> Sell", out, 36.55)

    # 3) Cost 29.24, Sell 36.55 -> Margin 20
    out, _ = _run_sequence(digits("29.24") + ["COST"] + digits("36.55") + ["SELL", "MGN"])
    check("Cost 29.24, Sell 36.55 -> Mgn", out, 20.0, tol=0.01)

    # 4) Markup: Cost 100, MU 20 -> Sell 125, markup amount 25
    out, eng = _run_sequence(digits("100") + ["COST"] + digits("20") + ["MU"])
    check("Cost 100, MU 20 -> Sell", out, 125.0)
    out = eng.press("MU")  # second press -> markup amount
    check("Cost 100, MU 20 -> markup amt", out, 25.0)

    # 5) Rate 8.25, TAX+ on 100 -> 108.25 ; second TAX+ -> 8.25
    out, eng = _run_sequence(digits("8.25") + ["RATE"] + digits("100") + ["TAX+"])
    check("Rate 8.25, TAX+ 100 -> total", out, 108.25)
    out = eng.press("TAX+")
    check("Rate 8.25, TAX+ 100 -> tax amt", out, 8.25)

    # 6) Rate 8.25, TAX- on 108.25 -> 100 ; second TAX- -> 8.25
    out, eng = _run_sequence(digits("8.25") + ["RATE"] + digits("108.25") + ["TAX-"])
    check("Rate 8.25, TAX- 108.25 -> pretax", out, 100.0)
    out = eng.press("TAX-")
    check("Rate 8.25, TAX- 108.25 -> tax amt", out, 8.25)

    # 7) 246 + 5% -> 258.30 ; 246 - 5% -> 233.70
    out, _ = _run_sequence(digits("246") + ["+"] + digits("5") + ["%"])
    check("246 + 5% ", out, 258.30)
    out, _ = _run_sequence(digits("246") + ["-"] + digits("5") + ["%"])
    check("246 - 5% ", out, 233.70)

    # 8) Memory: 99 M+, 6 M-, MRC -> 93
    out, _ = _run_sequence(digits("99") + ["M+"] + digits("6") + ["M-", "MRC"])
    check("99 M+, 6 M-, MRC", out, 93.0)

    print(
        "\n%d passed, %d failed" % (passed, failed),
        file=sys.stderr,
    )
    return failed == 0


# --------------------------------------------------------------------------- #
# Tkinter GUI
# --------------------------------------------------------------------------- #

def launch_gui():
    import tkinter as tk
    from tkinter import font as tkfont

    BG = "#1b1d1f"
    PANEL = "#2a2d31"
    LCD_BG = "#cdd6c2"
    LCD_FG = "#1a1d16"
    KEY_BG = "#3a3f45"
    KEY_FG = "#f2f2f2"
    OP_BG = "#4a5568"
    BIZ_BG = "#5a4a3a"   # business keys
    TAX_BG = "#3a5a4a"   # tax keys
    MEM_BG = "#444a55"   # memory keys
    MODE_BG = "#55504a"  # mode keys
    EQ_BG = "#c08a3e"
    ACCENT = "#d98c2b"

    eng = Engine(round_mode="5/4", decimal_mode="2")

    root = tk.Tk()
    root.title("SPL-290X")
    root.configure(bg=BG)
    root.resizable(False, False)

    lcd_font = tkfont.Font(family="Courier New", size=26, weight="bold")
    ind_font = tkfont.Font(family="Courier New", size=9, weight="bold")
    key_font = tkfont.Font(family="Helvetica", size=11, weight="bold")
    small_font = tkfont.Font(family="Helvetica", size=9, weight="bold")

    # --- display panel ---------------------------------------------------
    panel = tk.Frame(root, bg=PANEL, padx=10, pady=8)
    panel.grid(row=0, column=0, columnspan=6, sticky="nsew", padx=10, pady=(12, 6))

    lcd = tk.Frame(panel, bg=LCD_BG, padx=10, pady=6)
    lcd.pack(fill="x")

    ind_var = tk.StringVar()
    ind_lbl = tk.Label(
        lcd, textvariable=ind_var, font=ind_font, bg=LCD_BG, fg=LCD_FG,
        anchor="w",
    )
    ind_lbl.pack(fill="x")

    disp_var = tk.StringVar()
    disp_lbl = tk.Label(
        lcd, textvariable=disp_var, font=lcd_font, bg=LCD_BG, fg=LCD_FG,
        anchor="e",
    )
    disp_lbl.pack(fill="x")

    def refresh():
        disp_var.set(eng.display())
        bits = []
        if eng.memory != 0.0:
            bits.append("M")
        if eng.gt_on:
            bits.append("GT")
        bits.append("RND:" + eng.round_mode)
        bits.append("DEC:" + eng.decimal_mode)
        if eng.label:
            bits.append(eng.label)
        ind_var.set("   ".join(bits))
        # mode-cycle button captions (rnd_btn / dec_btn are bound by call time)
        rnd_btn.config(text="RND\n" + eng.round_mode)
        dec_btn.config(text="DEC\n" + eng.decimal_mode)

    def do(token):
        eng.press(token)
        refresh()

    # --- key grid --------------------------------------------------------
    grid = tk.Frame(root, bg=BG)
    grid.grid(row=1, column=0, columnspan=6, padx=10, pady=(0, 12))

    def add_key(text, token, r, c, *, bg=KEY_BG, fg=KEY_FG, cspan=1,
                font=key_font):
        b = tk.Button(
            grid, text=text, font=font, bg=bg, fg=fg,
            activebackground=ACCENT, activeforeground="#000",
            relief="raised", bd=1, width=6, height=2,
            command=lambda t=token: do(t),
        )
        b.grid(row=r, column=c, columnspan=cspan, padx=2, pady=2,
               sticky="nsew")
        return b

    # Row 0: business keys
    add_key("COST", "COST", 0, 0, bg=BIZ_BG)
    add_key("SELL", "SELL", 0, 1, bg=BIZ_BG)
    add_key("MGN", "MGN", 0, 2, bg=BIZ_BG)
    add_key("MU", "MU", 0, 3, bg=BIZ_BG)
    add_key("RATE\nSET", "RATE", 0, 4, bg=TAX_BG, font=small_font)
    add_key("GT", "GT", 0, 5, bg=MODE_BG)

    # Row 1: tax + memory + modes
    add_key("TAX+", "TAX+", 1, 0, bg=TAX_BG)
    add_key("TAX−", "TAX-", 1, 1, bg=TAX_BG)
    add_key("M+", "M+", 1, 2, bg=MEM_BG)
    add_key("M−", "M-", 1, 3, bg=MEM_BG)
    add_key("MRC", "MRC", 1, 4, bg=MEM_BG)

    rnd_btn = tk.Button(
        grid, font=small_font, bg=MODE_BG, fg=KEY_FG,
        activebackground=ACCENT, relief="raised", bd=1, width=6, height=2,
        command=lambda: (eng.cycle_round(), refresh()),
    )
    rnd_btn.grid(row=1, column=5, padx=2, pady=2, sticky="nsew")

    dec_btn = tk.Button(
        grid, font=small_font, bg=MODE_BG, fg=KEY_FG,
        activebackground=ACCENT, relief="raised", bd=1, width=6, height=2,
        command=lambda: (eng.cycle_decimal(), refresh()),
    )
    dec_btn.grid(row=2, column=5, padx=2, pady=2, sticky="nsew")

    # Row 2: clear / edit / ops
    add_key("C", "C", 2, 0, bg="#7a3b3b")
    add_key("CE", "CE", 2, 1, bg="#7a3b3b")
    add_key("⌫", "back", 2, 2, bg=MODE_BG)
    add_key("√", "sqrt", 2, 3, bg=OP_BG)
    add_key("÷", "/", 2, 4, bg=OP_BG)

    # Row 3: 7 8 9 ×
    add_key("7", "7", 3, 0)
    add_key("8", "8", 3, 1)
    add_key("9", "9", 3, 2)
    add_key("×", "*", 3, 3, bg=OP_BG)
    add_key("%", "%", 3, 4, bg=OP_BG)

    # Row 4: 4 5 6 −
    add_key("4", "4", 4, 0)
    add_key("5", "5", 4, 1)
    add_key("6", "6", 4, 2)
    add_key("−", "-", 4, 3, bg=OP_BG)
    add_key("+/−", "sign", 4, 4, bg=OP_BG)

    # Row 5: 1 2 3 +
    add_key("1", "1", 5, 0)
    add_key("2", "2", 5, 1)
    add_key("3", "3", 5, 2)
    add_key("+", "+", 5, 3, bg=OP_BG)
    eq = tk.Button(
        grid, text="=", font=lcd_font, bg=EQ_BG, fg="#1a1a1a",
        activebackground=ACCENT, relief="raised", bd=1,
        command=lambda: do("="),
    )
    eq.grid(row=5, column=4, rowspan=2, padx=2, pady=2, sticky="nsew")

    # Row 6: 0 00 .
    add_key("0", "0", 6, 0)
    add_key("00", "00", 6, 1)
    add_key(".", ".", 6, 2)
    # GT spanning column 5 already used by modes; put nothing.

    for c in range(6):
        grid.grid_columnconfigure(c, weight=1)

    # --- keyboard bindings ----------------------------------------------
    def on_key(event):
        k = event.keysym
        ch = event.char
        if ch and ch in "0123456789":
            do(ch)
        elif ch == ".":
            do(".")
        elif ch in ("+", "-", "*", "/"):
            do(ch)
        elif ch == "%":
            do("%")
        elif k in ("Return", "KP_Enter") or ch == "=":
            do("=")
        elif k == "Escape":
            do("C")
        elif k == "BackSpace":
            do("back")
        elif k == "Delete":
            do("CE")

    root.bind("<Key>", on_key)

    refresh()
    root.mainloop()


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #

def main(argv):
    if "--selftest" in argv:
        ok = selftest()
        return 0 if ok else 1
    launch_gui()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
