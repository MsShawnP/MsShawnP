# Shawn Phillips

Principal Consultant, Lailara LLC · KY

Most of my work happens in client systems and private repos. The public repos here are portfolio pieces, not my day-to-day output.

I build the data layer that operations actually runs on — validation, reporting, and decision frameworks for the systems upstream of fulfillment, payments, and analytics. Twenty-five years across incentive fulfillment, product master data, and operational reporting. The last twenty as a fractional Director of Operations and Solutions Architect for an incentive fulfillment platform, where data quality is the difference between a client renewal and an escalation.

Now building a second practice line: decision frameworks and tooling for specialty food brands scaling into national retail.

## What I Do

- Data hygiene across domains — transaction/purchase data, incentive and rebate payment data, product master (UPC/GTIN, GDSN, 1WorldSync), operational/fulfillment data
- Decision frameworks — velocity analysis, shelf defense, distribution strategy, promo ROI, SKU rationalization for CPG brands
- Custom analytics — Power BI dashboards, SQL-based reporting, Crystal Reports (1,000+ custom reports across industries)
- Data quality engineering — validation rules, audit scripts, and dashboards that catch bad data before submission
- Solution architecture — translating ambiguous business needs into clear technical specifications your team can implement

## Portfolio

The repos below are portfolio pieces. They range from a velocity decision tool for specialty food CEOs to acquisition due diligence on a public dataset, an Excel data-quality auditor, and product data validation tooling. Different problems, different tools (Python, Streamlit, R/Quarto, SQL). The common thread is the kind of input I'm willing to start with: data that hasn't been cleaned, validated, or interpreted yet, where the deliverable is the work of figuring out what's there and presenting it to someone who needs to act on it.

### Decision Frameworks

#### [retail-velocity-decision-tool](https://github.com/MsShawnP/retail-velocity-decision-tool)
Velocity decision tool for specialty food brands scaling into national retail. A CEO picks one of eight decisions — shelf defense, production planning, promo ROI, distribution expansion, distribution pruning, SKU rationalization, launch trajectory diagnostics, pricing power — and the tool surfaces the right velocity view to answer it. Includes a narrative deep dive ("The Charred Scallion Relish Problem") that traces one SKU through four decision modes, showing how a +15% YoY growth headline masked a 25% baseline velocity decline, $24,686 in wasted trade spend, and $723,842 in total hidden value destruction. Built on a synthetic 90-SKU dataset with 1.2M rows of weekly scan data across Walmart, Costco, Whole Foods, regional chains, UNFI, and DTC. Built in Python + Streamlit.

[Try it live →](https://velocity-tool.streamlit.app/)

### Demonstrations

#### [product-data-audit-demo](https://github.com/MsShawnP/product-data-audit-demo)
SQL diagnostic queries for auditing product master data quality in specialty food and CPG companies preparing for national retail. Covers GTIN/UPC validation, missing fields, data consistency, retailer readiness (Walmart, Costco, UNFI, Whole Foods), governance/staleness, and chargeback analysis. Built against the Cinderhaven Provisions dataset. SQL + Python.

### Data Quality Tools

#### [gtin-validator](https://github.com/MsShawnP/gtin-validator)
Product data validation tool for specialty food brands preparing for national retail. Validates GTINs against GS1 standards with retailer-specific context (Walmart, Costco, UNFI, 1WorldSync), generates branded PDF reports, and includes a prioritized fix roadmap, case GTIN-14 generator, and product data completeness analysis. Built in Python + Streamlit.

[Try it live →](https://msshawnp-gtin-validator-app-yz0mxn.streamlit.app/)

#### [data-hygiene-auditor](https://github.com/MsShawnP/data-hygiene-auditor)
Python CLI that audits Excel files for mixed formats, misused fields, placeholder floods, and phantom duplicates. Outputs HTML, Excel, and PDF reports.

#### [field-story-scorer](https://github.com/MsShawnP/field-story-scorer)
Python CLI that scores every column in an Excel file across five data quality dimensions. Includes strict cell-level type detection that catches mixed-type columns pandas silently coerces.

### Synthetic Datasets

#### [cinderhaven-data](https://github.com/MsShawnP/cinderhaven-data)
The shared dataset behind the Cinderhaven Provisions portfolio. A fictional ~$25M specialty food brand with 90 SKUs, ~1.19M rows of weekly scan data, and deliberate data-quality defects that cause every downstream problem in the dataset — chargebacks, slow launches, delisted SKUs. Includes the full generation pipeline and validation scripts. SQLite + Python.

### Due Diligence

#### [online-retail-analysis](https://github.com/MsShawnP/online-retail-analysis)
Acquisition due diligence portfolio piece. UCI Online Retail Dataset reframed as commercial DD — segment economics, customer-base trajectory, concentration risk, LTV modeling, and post-close action planning. Built in R + Quarto, deployed on Netlify. [Live report →](https://lailara-retail-analysis.netlify.app/)

## Background

Twenty-five years in incentive fulfillment and operational data. Twenty of those as fractional Director of Operations and Chief Solutions Architect for an incentive fulfillment platform — still active. Recent contract work auditing data quality for large language model training, reviewing and scoring response batches against accuracy, formatting, and domain knowledge standards.

HarvardX coursework in data science and Python/ML. Harvard Business School Online certificates in strategy execution and digital marketing strategy.

## Tools

Python · SQL · R · Streamlit · Quarto · Power BI · Crystal Reports · Excel (the serious kind) · SQLite · Plotly · pandas · VS Code · Claude Code · Netlify

## How I Work

Fractional engagements only. Fixed-fee or monthly retainer. No timesheets, no hourly billing. I work on outcomes, not hours. Typical first engagement is a 4–6 week scoped audit with a written assessment and remediation plan. From there we decide whether an ongoing retainer makes sense.
