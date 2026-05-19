# Shawn Phillips
**Principal Consultant, Lailara LLC · KY**

I work on the data layer between raw records and the systems that depend on them — validation, reporting, and decision tools for specialty food brands and CPG companies. Product data audits, quality engineering, and the infrastructure that keeps data clean after the audit is done.
The repos below are portfolio pieces. Different problems, different tools. The common thread: data that hasn't been cleaned, validated, or interpreted yet — and a deliverable built for someone who needs to act on what's in it.

## What I Do

- **Data hygiene across domains** — transaction/purchase data, incentive and rebate payment data, product master (UPC/GTIN, GDSN, 1WorldSync), operational/fulfillment data
- **Decision frameworks** — velocity analysis, shelf defense, distribution strategy, promo ROI, SKU rationalization for CPG brands
- **Custom analytics** — Power BI dashboards, SQL-based reporting, Crystal Reports (1,000+ custom reports across industries)
- **Data quality engineering** — validation rules, audit scripts, and dashboards that catch bad data before submission
- **Solution architecture** — translating ambiguous business needs into clear technical specifications your team can implement

## Portfolio

The repos below are portfolio pieces. They range from a velocity decision tool for specialty food CEOs to acquisition due diligence on a public dataset, an Excel data-quality auditor, and product data validation tooling. Different problems, different tools (Python, Dash, React, R/Quarto, SQL). The common thread is the kind of input I'm willing to start with: data that hasn't been cleaned, validated, or interpreted yet, where the deliverable is the work of figuring out what's there and presenting it to someone who needs to act on it.

### Decision Frameworks

**[product-data-health-audit](https://github.com/MsShawnP/product-data-health-audit)**
Product data readiness audit for a specialty food brand scaling into national retail. Finds $361,000/year in quantifiable cost from data defects, traces every chargeback to the specific field that caused it, and shows that 27 hours of data entry eliminates the entire problem. Produces five artifacts from one pipeline: an interactive HTML report, a two-page executive tearsheet, a Monday Morning operational dashboard, an eight-tab Excel workbook with triage list and broker intake checklist, and a standalone Data Debt Calculator. Includes GS1 Sunrise 2027 and FSMA Rule 204 compliance analysis. Built in R, Quarto, Postgres, and Shiny.

Landing page → https://msshawnp.github.io/product-data-health-audit/ · Data Debt Calculator → https://lailarallc.shinyapps.io/data-debt-calculator/

**[retail-velocity-decision-tool](https://github.com/MsShawnP/retail-velocity-decision-tool)**
Velocity decision tool for specialty food brands scaling into national retail. The default view is a portfolio health dashboard that surfaces risk indicators across every decision area. A CEO sees what needs attention immediately, then drills into the decision mode that answers it — shelf defense, production planning, promo ROI, distribution expansion, distribution pruning, SKU rationalization, launch trajectory diagnostics, or pricing power. Nine views total, each with a data grid, chart, and narrative insight. Built on a synthetic 90-SKU dataset with 1.2M rows of weekly scan data across Walmart, Costco, Whole Foods, regional chains, UNFI, and DTC. Python + Dash + AG Grid, hosted on Fly.io.

Try it live → https://retail-velocity-decision-tool.fly.dev

**[retailer-deduction-recovery](https://github.com/MsShawnP/retailer-deduction-recovery)**
Interactive decision tool that makes retailer deduction losses visible and actionable for a specialty food manufacturer. Traces every deduction through five compounding failures — no visibility, process gaps, weak evidence, inaccessible records, and missed dispute windows — and shows what's recoverable, what's preventable, and what each operational fix is worth. Ten connected views including Sankey flow with zoom-on-click, recovery simulation, cost-to-dispute filter, timeline pressure, and retailer scorecards. Built on synthetic data against the Cinderhaven Provisions dataset. React + Python, hosted on Cloudflare Pages.

Try it live → https://retailer-deduction-recovery.msshawnp.workers.dev/

**[trade-spend-data-diagnostic](https://github.com/MsShawnP/trade-spend-data-diagnostic)**
Trade spend diagnostic for a specialty food brand spending 17.3% of revenue on planned trade and losing an additional 4.0% to operational deductions — 21.3% all-in. A 7-tab Excel workbook that a CEO can open cold: executive pulse with waterfall chart and addressable improvement headline, leak diagnostic with double-dip detection, promo ROI with adjustable pre/post windows, retailer risk with net-net effective margin, full deduction ledger with translated reason codes, and methodology documentation. Interactive input cells let users adjust recovery rates, promo windows, and what-if trade rates and watch dependent values recalculate. Built on the Cinderhaven Data Platform (Postgres). Python + openpyxl.

**[short-ship-cost](https://github.com/MsShawnP/short-ship-cost)**
Interactive analysis tool that quantifies the full cost of short-shipping orders for a specialty food brand operating make-to-order with no inventory buffer. Calculates eight cost dimensions — lost revenue, OTIF fines, chargebacks, deauthorization, DTC cancellations, margin leakage, distributor returns, and triage labor — from the gap between original orders and what actually shipped. Parameter panel lets users adjust fine rates, thresholds, and margins and watch costs recalculate live. Buffer simulation shows cost recovery at increasing fill rates, including the deauthorization cliff at 90%. Exportable Economist-style PDF via print CSS. Built on synthetic order data against the Cinderhaven Provisions dataset. React + Python, hosted on Cloudflare Pages.

Try it live → https://short-ship-cost.msshawnp.workers.dev/

### Data Quality Tools

**[edi-preflight](https://github.com/MsShawnP/edi-preflight)**
Free web tool for specialty food brands doing EDI by hand. Parses inbound 850 Purchase Orders into structured data with CSV/PDF export, and validates outbound 856 Advance Ship Notices against retailer-specific specs with severity-tagged findings and chargeback-dollar attribution. Supports Walmart, Amazon, UNFI, KeHE, and Costco. Stateless — no data stored. Python + FastAPI + HTMX, hosted on Fly.io.

Try it live → https://edi-preflight.fly.dev

**[gtin-validator](https://github.com/MsShawnP/gtin-validator)**
Product data validation tool for specialty food brands preparing for national retail. Validates GTINs against GS1 standards with retailer-specific context (Walmart, Costco, UNFI, 1WorldSync), generates branded PDF reports, and includes a prioritized fix roadmap, case GTIN-14 generator, and product data completeness analysis. FastAPI + React, hosted on Render.

Try it live → https://gtin-validator.onrender.com

**[data-hygiene-auditor](https://github.com/MsShawnP/data-hygiene-auditor)**
Python CLI that audits Excel files for mixed formats, misused fields, placeholder floods, and phantom duplicates. Outputs HTML, Excel, and PDF reports.

**[datascope](https://github.com/MsShawnP/datascope)**
Data quality diagnostic CLI that reads each cell's actual type (not what pandas infers), detects mixed types, sentinel values, format inconsistencies, and cardinality anomalies, then generates a professional report in plain English. Supports Excel, CSV, and Parquet. Four output formats: PDF, HTML, annotated Excel, and JSON. pip-installable (`datascope-dq`). Python + openpyxl + reportlab.

### Data Infrastructure

**[cinderhaven-data-platform](https://github.com/MsShawnP/cinderhaven-data-platform)**
Modern data platform for the Cinderhaven Provisions portfolio. Postgres + dbt + Dagster pipeline covering 23 source tables, 34 transformation models, and 132 data quality tests. Ingests from the generation layer, transforms raw → staging → marts, and serves as the analytical source of truth for all portfolio projects above. Hosted on Fly.io. Python + dbt + Dagster + PostgreSQL.

**[cinderhaven-data](https://github.com/MsShawnP/cinderhaven-data)**
The generation layer for the Cinderhaven Provisions portfolio dataset. A fictional ~$25M specialty food brand with 90 SKUs, ~1.19M rows of weekly scan data, and deliberate data-quality defects that cause every downstream problem in the dataset — chargebacks, slow launches, delisted SKUs. Includes the full generation pipeline and validation scripts. The data platform ingests this SQLite database into Postgres. SQLite + Python.

### Developer Workflow

**[claude-solo-dev-workflow](https://github.com/MsShawnP/claude-solo-dev-workflow)**
Solo developer workflow for Claude Code and Claude chat. Templates, slash commands, and reference materials used across all portfolio projects.

### Due Diligence

**[online-retail-analysis](https://github.com/MsShawnP/online-retail-analysis)**
Acquisition due diligence portfolio piece. UCI Online Retail Dataset reframed as commercial DD — segment economics, customer-base trajectory, concentration risk, LTV modeling, and post-close action planning. Built in R + Quarto, deployed on Cloudflare Pages. Live report → https://online-retail-analysis.msshawnp.workers.dev/

## Background

Twenty-five years in incentive fulfillment and operational data. Twenty of those as fractional Director of Operations and Chief Solutions Architect for an incentive fulfillment platform — still active. Recent contract work auditing data quality for large language model training, reviewing and scoring response batches against accuracy, formatting, and domain knowledge standards.

HarvardX coursework in data science and Python/ML. Harvard Business School Online certificates in strategy execution and digital marketing strategy.

## Tools

Python · SQL · R · React · Dash · Shiny · Quarto · Excel · PostgreSQL · dbt · Dagster · SQLite · Plotly · pandas · FastAPI · Fly.io · Cloudflare Pages · Render · GitHub Pages · VS Code · Claude Code

## How I Work

Fractional engagements only. Fixed-fee or monthly retainer. No timesheets, no hourly billing. I work on outcomes, not hours.
