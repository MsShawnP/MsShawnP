# Hey, I'm Shawn.

I'm the Principal Consultant at **[Lailara LLC](https://lailarallc.com)** — data hygiene and
analytics for specialty food and CPG brands scaling into national retail. I find the money
leaking through product data, deductions, and trade spend, and tell you exactly which field
it's leaking from.

I'm not a software engineer by training. Twenty-five years of operations and
incentive-fulfillment work taught me to build tools when the thing I need doesn't exist —
and to publish them so other people can use them too.

Everything below falls into four buckets: Python packages you can `pip install`, free
browser tools, worked analytical engagements, and the internal tooling I consult with.

---

## Install with pip

- **[data-hygiene-auditor](https://github.com/MsShawnP/data-hygiene-auditor)** — A linter for your
  data. Audits Excel/CSV files for mixed formats, misused fields, placeholder floods, and phantom
  duplicates; outputs HTML, Excel, and PDF reports.
  `pip install data-hygiene-auditor` · [PyPI](https://pypi.org/project/data-hygiene-auditor/)
- **[datascope](https://github.com/MsShawnP/datascope)** — Python CLI that profiles every column in an
  Excel file, flags hidden data-quality problems (mixed types, sentinel values, missing data,
  cardinality anomalies) in plain English, and outputs PDF, HTML, JSON, or annotated-Excel reports.
  Includes strict cell-level type detection that catches mixed-type columns pandas silently coerces.
  `pip install datascope-dq` · [PyPI](https://pypi.org/project/datascope-dq/)

## Use in your browser — free, no login

- **[GTIN Validator](https://gtin.lailarallc.com)** — product data validated against GS1 standards
  with retailer-specific context; branded PDF report with a fix roadmap
- **[EDI Preflight](https://edi.lailarallc.com)** — checks 850s and 856s against retailer specs
  (Walmart, Amazon, UNFI, KeHE, and more) before you submit
- **[Retail Readiness Scorecard](https://lailarallc.com/scorecard)** — eight-dimension readiness
  self-assessment for a retailer launch, ten minutes, PDF readout
- **[Cost of Saying Yes](https://launch-cost.lailarallc.com)** — month-by-month cash model for a
  major retailer launch, because revenue projections hide the trough

## Worked engagements (Cinderhaven Provisions)

Full analytical engagements on a synthetic $25M specialty food brand — the data is invented so the
methodology can be shown end to end, and the dollar figures are real outputs of the pipelines.
Highlights:

- **[product-data-health-audit](https://github.com/MsShawnP/product-data-health-audit)** — every
  chargeback traced to the product-master field that caused it (~$93K/yr in data-defect
  chargebacks quantified)
- **[retailer-deduction-recovery](https://github.com/MsShawnP/retailer-deduction-recovery)** —
  16,917 deductions traced through five compounding failures; ~42% win rate per disputed
  dollar, but two-thirds of deductions are never filed
- **[cinderhaven-data-platform](https://github.com/MsShawnP/cinderhaven-data-platform)** — the data
  platform underneath it all: source-to-mart pipelines, quality testing, orchestration, lineage
  (Python · Postgres · dbt · Dagster)

The rest — trade spend forensics, OTIF reconciliation, SKU scoring, channel profitability, demand
planning, shelf intelligence — lives at **[lailarallc.com/work](https://lailarallc.com/work)**.

## Consultant tooling

- **[item-setup-form-preflight](https://github.com/MsShawnP/item-setup-form-preflight)** — typed
  validation against codified retailer schemas; catches new-item rejections before submission
- **[dimension-weight-integrity](https://github.com/MsShawnP/dimension-weight-integrity)** —
  dim-weight validation for the defects behind freight chargebacks
- **[internal-data-anonymizer](https://github.com/MsShawnP/internal-data-anonymizer)** — guided
  column-by-column anonymization with deterministic, format-preserving mappings
- **[data-differences-tool](https://github.com/MsShawnP/data-differences-tool)** — diff two tabular
  files: rows added, removed, modified, with before/after values

## How I work

Solo developer, Claude Code as pair programmer, phase-gated workflow with commit gates —
packaged at [claude-solo-dev-workflow](https://github.com/MsShawnP/claude-solo-dev-workflow).

**Stack:** Python · R · SQL · Quarto · dbt · Postgres · React · Power BI · Excel (the serious kind)

---

📍 Kentucky · [lailarallc.com](https://lailarallc.com) ·
[LinkedIn](https://www.linkedin.com/in/shawn-phillips-b383b3149)
