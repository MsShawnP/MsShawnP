# Hey, I'm Shawn.

I'm the Principal Consultant at **[Lailara LLC](https://lailarallc.com)** — data hygiene and
analytics for specialty food and CPG brands scaling into national retail. I find the money leaking
through product data, deductions, and trade spend, and tell you exactly which field it's leaking from.

I'm not a software engineer by training. Twenty-five years of operations and incentive-fulfillment
work taught me to build the tool when the thing I need doesn't exist — and to publish it so other
people can use it too.

**41 public tools. 31 of them running live in your browser right now.** Two on PyPI. No login, no
demo request, no gate.

---

## Install with pip

| Package | What it does | Install |
|---|---|---|
| **[data-hygiene-auditor](https://github.com/MsShawnP/data-hygiene-auditor)** | A linter for your data — mixed formats, misused fields, placeholder floods, phantom duplicates. HTML, Excel, and PDF reports. | `pip install data-hygiene-auditor` · [PyPI](https://pypi.org/project/data-hygiene-auditor/) |
| **[datascope](https://github.com/MsShawnP/datascope)** | Profiles every column in an Excel file and explains the data-quality problems in plain English. Catches mixed-type columns pandas silently coerces. | `pip install datascope-dq` · [PyPI](https://pypi.org/project/datascope-dq/) |

## Use in your browser — free, no login

Bring your own file. Nothing is stored.

| Tool | What it does | Live |
|---|---|---|
| **[GTIN Validator](https://github.com/MsShawnP/gtin-validator)** | Product data checked against GS1 standards with retailer-specific context. Branded PDF with a fix roadmap. | [gtin.lailarallc.com](https://gtin.lailarallc.com) |
| **[EDI Preflight](https://github.com/MsShawnP/edi-preflight)** | Parses 850s and validates 856s against Walmart, Amazon, UNFI, KeHE, and Costco specs. | [edi.lailarallc.com](https://edi.lailarallc.com) |
| **[Item Setup Form Preflight](https://github.com/MsShawnP/item-setup-form-preflight)** | Typed validation against codified retailer schemas. Catches new-item rejections before you submit. | [preflight.lailarallc.com](https://preflight.lailarallc.com) |
| **[Data Differences Tool](https://github.com/MsShawnP/data-differences-tool)** | Compare two tabular files: rows added, removed, modified, with before/after values. | [diff.lailarallc.com](https://diff.lailarallc.com) |
| **[Recall Blast Radius](https://github.com/MsShawnP/recall-blast-radius)** | Lot-genealogy tracer that answers "how big is our recall?" in seconds. | [recall.lailarallc.com](https://recall.lailarallc.com) |
| **[The Question Engine](https://github.com/MsShawnP/the-question-engine)** | Fifteen questions every specialty-food CEO asks, each answered in 30 seconds with a verdict, one chart, three numbers. | [ask.lailarallc.com](https://ask.lailarallc.com) |
| **[Retail Readiness Scorecard](https://github.com/MsShawnP/retail-readiness-scorecard)** | 12–18 adaptive questions across eight dimensions. Downloadable PDF verdict on launch readiness. | [lailarallc.com/scorecard](https://lailarallc.com/scorecard) |
| **[Data Standards Cheat Sheet](https://github.com/MsShawnP/data-standards-cheat-sheet)** | One-page reference on GTIN, GDSN, item-setup, and freight-class rules. Downloadable PDF. | — |

## Where the money leaks

Deductions, trade spend, and the gap between invoiced and collected.

| Tool | What it does | Live |
|---|---|---|
| **[Retailer Deduction Recovery](https://github.com/MsShawnP/retailer-deduction-recovery)** | 16,917 deductions traced through five compounding failures. ~42% win rate per disputed dollar — but two-thirds are never filed. | [deductions.lailarallc.com](https://deductions.lailarallc.com) |
| **[Chargeback Prediction Model](https://github.com/MsShawnP/chargeback-prediction-model)** | Predicts which retailer deductions escalate and which are recoverable. Python + scikit-learn. | [chargeback.lailarallc.com](https://chargeback.lailarallc.com) |
| **[Trade Spend Leakage](https://github.com/MsShawnP/trade-spend-leakage)** | Forensic detection of double-funded promos, phantom promos, and rate discrepancies. Reranks retailers by net revenue. | [trade-spend.lailarallc.com](https://trade-spend.lailarallc.com) |
| **[Contract to Cash](https://github.com/MsShawnP/contract-to-cash)** | Traces where money leaks between invoice and cash receipt. For every dollar invoiced, 83 cents arrived. | [cash.lailarallc.com](https://cash.lailarallc.com) |
| **[Channel Profitability Analysis](https://github.com/MsShawnP/channel-profitability-analysis)** | Five-layer cost waterfall. Contribution margin across 10 retail, distributor, and DTC channels. | [channels.lailarallc.com](https://channels.lailarallc.com) |
| **[Where the Money Comes From](https://github.com/MsShawnP/where-the-money-comes-from)** | Which channel actually pays after all deductions — and is the capital allocation wrong? React + D3. | [capital.lailarallc.com](https://capital.lailarallc.com) |
| **[Trade Spend Data Diagnostic](https://github.com/MsShawnP/trade-spend-data-diagnostic)** | 7-tab Excel: executive pulse, leak diagnostic, promo ROI, retailer risk, deduction ledger. | — |
| **[Remittance Stub Parsing](https://github.com/MsShawnP/remittance-stub-parsing)** | Turns unstructured remittance stubs into reconcilable line-item data. | — |

## Sales penetration series

Five ways to answer the same question: is growth real, or are we buying it?

| Tool | What it does | Live |
|---|---|---|
| **[SpinRate](https://github.com/MsShawnP/spinrate-sales-penetration)** | Separates distribution gains from velocity gains. SPPD, ACV%, door counts. | [spinrate.lailarallc.com](https://spinrate.lailarallc.com) |
| **[Void Finder](https://github.com/MsShawnP/voidfinder-sales-penetration)** | Authorized but not scanning. Every void dollarized from comparable-store median velocity and ranked into a broker work list. | [voidfinder.lailarallc.com](https://voidfinder.lailarallc.com) |
| **[DoorMath](https://github.com/MsShawnP/doormath-sales-penetration)** | Door counts, ACV%, TDP trends, and authorization gap analysis. | [doormath.lailarallc.com](https://doormath.lailarallc.com) |
| **[Decompose](https://github.com/MsShawnP/decompose-sales-penetration)** | Splits period-over-period sales change into households × frequency × spend per trip, reconciled to the exact delta with a Shapley allocation. | [decompose.lailarallc.com](https://decompose.lailarallc.com) |
| **[Trial vs. Repeat](https://github.com/MsShawnP/trial-vs-repeat)** | How many triers came back — and whether penetration growth is adoption or expensive sampling. | [leakybucket.lailarallc.com](https://leakybucket.lailarallc.com) |

## Decision tools

The calls that cost real money when made by reflex instead of analysis.

| Tool | What it does | Live |
|---|---|---|
| **[The Ten Decisions](https://github.com/MsShawnP/the-ten-decisions)** | The framework: ten operating decisions that cost a growing brand $1.4M–$3.1M a year. | [lailarallc.com/the-ten-decisions](https://lailarallc.com/the-ten-decisions) |
| **[Retail Velocity Decision Tool](https://github.com/MsShawnP/retail-velocity-decision-tool)** | Eight decisions — shelf defense, production planning, promo ROI, expansion, pricing power — on a 1.2M-row dataset. | [velocity.lailarallc.com](https://velocity.lailarallc.com) |
| **[The Cost of Saying Yes](https://github.com/MsShawnP/cost-of-saying-yes)** | First-year economics of a major retailer launch. Cash trough, break-even month, CFO-grade Excel export. | [launch-cost.lailarallc.com](https://launch-cost.lailarallc.com) |
| **[Short Ship Cost](https://github.com/MsShawnP/short-ship-cost)** | Eight cost dimensions of short-shipping, with buffer simulation and exportable PDF. | [shortships.lailarallc.com](https://shortships.lailarallc.com) |
| **[Retailer Scorecard Renegotiation Simulator](https://github.com/MsShawnP/retailer-scorecard-renegotiation-simulator)** | Cost-to-serve model you can renegotiate against. React + Python. | [retailer-scorecard.lailarallc.com](https://retailer-scorecard.lailarallc.com) |
| **[SKU Rationalization Framework](https://github.com/MsShawnP/sku-rationalization-framework)** | Five scoring dimensions, four action buckets, interactive portfolio view. | [sku.lailarallc.com](https://sku.lailarallc.com) |
| **[Production Demand Forecast](https://github.com/MsShawnP/production-demand-forecast)** | S&OP planning: demand signals, capacity constraints, seasonal patterns. | [forecast.lailarallc.com](https://forecast.lailarallc.com) |
| **[Competitive Shelf Intelligence](https://github.com/MsShawnP/competitive-shelf-intelligence)** | Pricing, placement, and assortment tracked across retailers. | [competitive.lailarallc.com](https://competitive.lailarallc.com) |
| **[Monday Morning Report](https://github.com/MsShawnP/monday-morning-report)** | Three critical Monday numbers, tiered by growth stage. Python + openpyxl. | — |

## Supply chain and fulfillment

| Tool | What it does | Live |
|---|---|---|
| **[OTIF Blind Spot](https://github.com/MsShawnP/otif-blind-spot)** | Reconciles internal fulfillment metrics against retailer scorecards and quantifies the gap. | [otif.lailarallc.com](https://otif.lailarallc.com) |
| **[EDI Reconciliation Tool](https://github.com/MsShawnP/edi-reconciliation-tool)** | Content-level reconciliation across the full PO lifecycle. Every mismatch, dollar-ranked. | [reconcile.lailarallc.com](https://reconcile.lailarallc.com) |
| **[Dimension & Weight Integrity](https://github.com/MsShawnP/dimension-weight-integrity)** | Catches the dim-weight defects behind freight chargebacks and compliance fines. | [dimensions.lailarallc.com](https://dimensions.lailarallc.com) |

## Data foundations

The layer everything above depends on.

| Tool | What it does | Live |
|---|---|---|
| **[Cinderhaven Data Platform](https://github.com/MsShawnP/cinderhaven-data-platform)** | The platform underneath it all — source-to-mart pipelines, quality testing, orchestration, lineage. Python · Postgres · dbt · Dagster. | — |
| **[Product Master Data Model](https://github.com/MsShawnP/product-master-data-model)** | The data model a product master should have — documented, contracted, running on Postgres + dbt. | [master.lailarallc.com](https://master.lailarallc.com) |
| **[Product Data Health Audit](https://github.com/MsShawnP/product-data-health-audit)** | Five artifacts from one R + Quarto pipeline: HTML report, executive tearsheet, dashboard, Excel workbook, Shiny calculator. | [audit.lailarallc.com](https://audit.lailarallc.com) |
| **[Internal Data Anonymizer](https://github.com/MsShawnP/internal-data-anonymizer)** | Column-by-column anonymization with deterministic mappings, format-preserving fakes, and reverse lookup. | — |

## How I build

| Repo | What it does |
|---|---|
| **[claude-solo-dev-workflow](https://github.com/MsShawnP/claude-solo-dev-workflow)** | Templates, slash commands, and reference material for running portfolio projects solo. |
| **[claude-solo-dev-project-improvement-workflow](https://github.com/MsShawnP/claude-solo-dev-project-improvement-workflow)** | Phase-gated improvement workflow — audit, plan, code review, dependency audit, README refresh. |

---

Every tool above is built on realistic CPG data shapes and solves a problem I hit in an actual
engagement. If one of them describes your week, that's usually a good sign we should talk.

**[lailarallc.com](https://lailarallc.com)** · [Selected work](https://lailarallc.com/work) ·
[LinkedIn](https://www.linkedin.com/in/shawn-phillips-b383b3149) · shawn@lailarallc.com
