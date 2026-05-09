# Shawn Phillips
**Principal Consultant, Lailara LLC · KY**

Most of my work happens in client systems and private repos. The public repos here are portfolio pieces, not my day-to-day output.

I build the data layer that operations actually runs on — validation, reporting, and decision frameworks for the systems upstream of fulfillment, payments, and analytics. Twenty-five years across incentive fulfillment, product master data, and operational reporting. The last twenty as a fractional Director of Operations and Solutions Architect for an incentive fulfillment platform, where data quality is the difference between a client renewal and an escalation.

Now building a second practice line: decision frameworks and tooling for specialty food brands scaling into national retail.

## What I Do

- **Data hygiene across domains** — transaction/purchase data, incentive and rebate payment data, product master (UPC/GTIN, GDSN, 1WorldSync), operational/fulfillment data
- **Decision frameworks** — velocity analysis, shelf defense, distribution strategy, promo ROI, SKU rationalization for CPG brands
- **Custom analytics** — Power BI dashboards, SQL-based reporting, Crystal Reports (1,000+ custom reports across industries)
- **Data quality engineering** — validation rules, audit scripts, and dashboards that catch bad data before submission
- **Solution architecture** — translating ambiguous business needs into clear technical specifications your team can implement

## Portfolio

The repos below are portfolio pieces. They range from a velocity decision tool for specialty food CEOs to acquisition due diligence on a public dataset, an Excel data-quality auditor, and product data validation tooling. Different problems, different tools (Python, Streamlit, R/Quarto, SQL). The common thread is the kind of input I'm willing to start with: data that hasn't been cleaned, validated, or interpreted yet, where the deliverable is the work of figuring out what's there and presenting it to someone who needs to act on it.

### Decision Frameworks

**[product-data-health-audit](https://github.com/MsShawnP/product-data-health-audit)**
Product data readiness audit for a specialty food brand scaling into national retail. Finds $361,000/year in quantifiable cost from data defects, traces every chargeback to the specific field that caused it, and shows that 27 hours of data entry eliminates the entire problem. Produces five artifacts from one pipeline: an interactive HTML report, a two-page executive tearsheet, a Monday Morning operational dashboard, an eight-tab Excel workbook with triage list and broker intake checklist, and a standalone Data Debt Calculator. Includes GS1 Sunrise 2027 and FSMA Rule 204 compliance analysis. Built in R, Quarto, SQLite, and Shiny.

[Landing page →](https://msshawnp.github.io/product-data-health-audit/) · [Data Debt Calculator →](https://lailarallc.shinyapps.io/data-debt-calculator/)

**[retail-velocity-decision-tool](https://github.com/MsShawnP/retail-velocity-decision-tool)**
Velocity decision tool for specialty food brands scaling into national retail. A CEO picks one of eight decisions — shelf defense, production planning, promo ROI, distribution expansion, distribution pruning, SKU rationalization, launch trajectory diagnostics, pricing power — and the tool surfaces the right velocity view to answer it. Includes a narrative deep dive ("The Charred Scallion Relish Problem") that traces one SKU through four decision modes, showing how a +15% YoY growth headline masked a 25% baseline velocity decline, $24,686 in wasted trade spend, and $723,842 in total hidden value destruction. Built on a synthetic 90-SKU dataset with 1.2M rows of weekly scan data across Walmart, Costco, Whole Foods, regional chains, UNFI, and DTC. Built in Python + Streamlit.

[Try it live →](https://retail-velocity-decision-tool.streamlit.app/)

**[retailer-deduction-recovery](https://github.com/MsShawnP/retailer-deduction-recovery)**
Interactive decision tool that makes retailer deduction losses visible and actionable for a specialty food manufacturer. Traces every deduction through five compounding failures — no visibility, process gaps, weak evidence, inaccessible records, and missed dispute windows — and shows what's recoverable, what's preventable, and what each operational fix is worth. Ten connected views including Sankey flow with zoom-on-click, recovery simulation, cost-to-dispute filter, timeline pressure, and retailer scorecards. Built on synthetic data against the Cinderhaven Provisions dataset. React + Python, hosted on Cloudflare Pages.

[Try it live →](https://retailer-deduction-recovery.msshawnp.workers.dev/)

**[short-ship-cost](https://github.com/MsShawnP/short-ship-cost)**
Interactive analysis tool that quantifies the full cost of short-shipping orders for a specialty food brand operating make-to-order with no inventory buffer. Calculates eight cost dimensions — lost revenue, OTIF fines, chargebacks, deauthorization, DTC cancellations, margin leakage, distributor returns, and triage labor — from the gap between original orders and what actually shipped. Parameter panel lets users adjust fine rates, thresholds, and margins and watch costs recalculate live. Buffer simulation shows cost recovery at increasing fill rates, including the deauthorization cliff at 90%. Exportable Economist-style PDF via print CSS. Built on synthetic order data against the Cinderhaven Provisions dataset. React + Python, hosted on Netlify.

[Try it live →](https://short-ship-cost.netlify.app/)

### Demonstrations

**[product-data-audit-demo](https://github.com/MsShawnP/product-data-audit-demo)**
SQL diagnostic query library and fast HTML audit report that feeds the full product data readiness audit above. 53 queries covering GTIN/UPC validation, missing fields, retailer readiness, and chargeback analysis. Built against the Cinderhaven Provisions dataset. SQL + Python.

### Data Quality Tools

**[gtin-validator](https://github.com/MsShawnP/gtin-validator)**
Product data validation tool for specialty food brands preparing for national retail. Validates GTINs against GS1 standards with retailer-specific context (Walmart, Costco, UNFI, 1WorldSync), generates branded PDF reports, and includes a prioritized fix roadmap, case GTIN-14 generator, and product data completeness analysis. Built in Python + Streamlit.

[Try it live →](https://gtin-validator.streamlit.app/)

**[data-hygiene-auditor](https://github.com/MsShawnP/data-hygiene-auditor)**
Python CLI that audits Excel files for mixed formats, misused fields, placeholder floods, and phantom duplicates. Outputs HTML, Excel, and PDF reports.

**[field-story-scorer](https://github.com/MsShawnP/field-story-scorer)**
Python CLI that scores every column in an Excel file across five data quality dimensions. Includes strict cell-level type detection that catches mixed-type columns pandas silently coerces.

### Synthetic Datasets

**[cinderhaven-data](https://github.com/MsShawnP/cinderhaven-data)**
The shared dataset behind the Cinderhaven Provisions portfolio. A fictional ~$25M specialty food brand with 90 SKUs, ~1.19M rows of weekly scan data, and deliberate data-quality defects that cause every downstream problem in the dataset — chargebacks, slow launches, delisted SKUs. Includes the full generation pipeline and validation scripts. SQLite + Python.

### Due Diligence

**[online-retail-analysis](https://github.com/MsShawnP/online-retail-analysis)**
Acquisition due diligence portfolio piece. UCI Online Retail Dataset reframed as commercial DD — segment economics, customer-base trajectory, concentration risk, LTV modeling, and post-close action planning. Built in R + Quarto, deployed on Netlify. [Live report →](https://online-retail-analysis.netlify.app/)

## Background

Twenty-five years in incentive fulfillment and operational data. Twenty of those as fractional Director of Operations and Chief Solutions Architect for an incentive fulfillment platform — still active. Recent contract work auditing data quality for large language model training, reviewing and scoring response batches against accuracy, formatting, and domain knowledge standards.

HarvardX coursework in data science and Python/ML. Harvard Business School Online certificates in strategy execution and digital marketing strategy.

## Tools

Python · SQL · R · React · Shiny · Streamlit · Quarto · Excel (the serious kind) · SQLite · Plotly · pandas · GitHub Pages · Cloudflare Pages · VS Code · Claude Code · Netlify

## How I Work

Fractional engagements only. Fixed-fee or monthly retainer. No timesheets, no hourly billing. I work on outcomes, not hours.
