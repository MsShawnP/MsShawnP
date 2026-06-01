# SPL-290X — software replica of the Staples SPL-290X business/tax calculator

A portable Windows calculator app that replicates the Staples SPL-290X
business/tax desktop calculator. Single-file, no install, no console window.

- **`spl290x.py`** — the whole app (GUI + engine + self-test). Stdlib only
  (Tkinter), so the packaged exe stays small and bundles cleanly with no
  third-party runtime dependencies.

## Run from source

```
python spl290x.py            # launch the GUI
python spl290x.py --selftest # run acceptance tests (prints PASS/FAIL to stderr)
```

## Build the portable exe

```
pyinstaller --onefile --windowed --name SPL-290X spl290x.py
```

Output: **`dist/SPL-290X.exe`** — onefile, windowed (no console), runs
standalone with no install. Helper scripts `build.bat` (Windows) and
`build.sh` run the self-test first, then build.

> PyInstaller does not cross-compile. To produce a Windows `.exe` you must run
> the build on Windows (Python from python.org includes Tkinter).

## Keypad

- Digits `0–9`, `.`, `00`, operators `+ − × ÷`, `=`, `%`, `√`, `+/−`, `C`,
  `CE`, and `⌫` backspace.
- **Business:** `COST`, `SELL`, `MGN`, `MU`.
- **Tax:** `TAX+`, `TAX−`, `RATE SET`.
- **Memory:** `M+`, `M−`, `MRC` (recall, second press clears).
- **GT** grand-total accumulation toggle.
- **Modes** (cycling buttons): `RND` = UP / 5/4 / CUT, `DEC` = F / 3 / 2 / 0 / ADD2.
- 12-digit, right-aligned, comma-grouped display with mode indicators (M, GT,
  active rounding and decimal mode, and the COST/SELL/MGN%/TAX label).

### Keyboard

`0–9 . + - * /` keyed directly · `Enter` = `=` · `Esc` = clear (C) ·
`Backspace` = delete last digit · `Delete` = CE · `%` = percent.

## Function math

**Cost / Sell / Margin** (GAAP margin-on-sell) — enter any two, press the
third key to solve it:

```
Margin% = (Sell − Cost) / Sell × 100
Sell    = Cost / (1 − Margin/100)      # given Cost & Margin
Cost    = Sell × (1 − Margin/100)      # given Sell & Margin
```

**Markup (MU).** Note: the written spec gave `Sell = Cost × (1 + MU/100)`
(which yields 120 for Cost 100 / MU 20), but the **verified acceptance test**
requires Cost 100 / MU 20 → **Sell 125, markup amount 25**. The acceptance test
is authoritative, so MU uses the margin-style relation
`Sell = Cost / (1 − MU/100)`, with markup amount `Sell − Cost`. Second press of
MU shows the markup amount.

**Tax** (rate stored in-session via `RATE SET`):

```
TAX+ : total  = amount × (1 + rate/100)   # amount is pre-tax
TAX− : pretax = amount / (1 + rate/100)   # amount is tax-inclusive
```

Pressing `TAX+`/`TAX−` a second time shows the tax amount alone.

**Rounding / decimal modes** apply to displayed results. `F` = floating (no
rounding); `ADD2` auto-inserts two decimals on raw entry.

## Acceptance tests (all pass — see `--selftest`)

| Input | Result |
|---|---|
| Sell 36.55, Margin 20 | Cost 29.24 |
| Cost 29.24, Margin 20 | Sell 36.55 |
| Cost 29.24, Sell 36.55 | Margin 20 |
| Cost 100, MU 20 | Sell 125, markup amount 25 |
| Rate 8.25, TAX+ on 100 | 108.25; second TAX+ → 8.25 |
| Rate 8.25, TAX− on 108.25 | 100; second TAX− → 8.25 |
| 246 + 5% | 258.30 |
| 246 − 5% | 233.70 |
| 99 M+, 6 M−, MRC | 93 |
