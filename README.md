# About Me

Most of my work happens in client systems and private repos. The public repos here are portfolio pieces, not my day-to-day output.

**Lailara LLC · Director of Operations, Chief Solutions Architect at Incentive Insights · Data hygiene and reporting for transaction, incentive, and product data**

I clean, validate, and build the reporting layer for the systems your business actually runs on — the hygiene work that sits upstream of fulfillment, payments, and analytics, so the data flowing through is already right.

Twenty-five years in incentive fulfillment and operational data. The last twenty running operations and architecting client solutions at a lean, bootstrapped startup. Data quality for me isn't theoretical; it's the difference between a client renewal and an escalation, and I've lived the consequences of both.

---

## What I Do

- **Data hygiene** across domains — transaction/purchase data, incentive and rebate payment data, product master (UPC/GTIN, GDSN, 1WorldSync), operational/fulfillment data
- **Custom analytics** — Power BI dashboards, SQL-based reporting, Crystal Reports (1,000+ custom reports across industries)
- **Data quality engineering** — validation rules, audit scripts, and dashboards that catch bad data before submission
- **Solution architecture** — translating ambiguous business needs into clear technical specifications your team can implement

---

## Portfolio

The repos below are portfolio pieces. They range from a velocity decision tool for specialty food CEOs to acquisition due diligence on a public dataset, an Excel data-quality auditor, and product data validation tooling. Different problems, different tools (Python, Streamlit, R/Quarto, SQL). The common thread is the kind of input I'm willing to start with: data that hasn't been cleaned, validated, or interpreted yet, where the deliverable is the work of figuring out what's there and presenting it to someone who needs to act on it.

### [retail-velocity-decision-tool](https://github.com/MsShawnP/retail-velocity-decision-tool)
Velocity decision tool for specialty food brands scaling into national retail. A CEO picks one of eight decisions — shelf defense, production planning, promo ROI, distribution expansion, distribution pruning, SKU rationalization, launch trajectory diagnostics, pricing power — and the tool surfaces the right velocity view to answer it. Built on a synthetic 90-SKU dataset with 1.2M rows of weekly scan data across Walmart, Costco, Whole Foods, regional chains, UNFI, and DTC. Includes retailer-specific pricing, promotional patterns, data-quality-driven chargebacks, and a full data generation pipeline. Built in Python + Streamlit.

Try it live → https://velocity-tool.streamlit.app/

### [online-retail-analysis](https://github.com/MsShawnP/online-retail-analysis)
Acquisition due diligence portfolio piece. UCI Online Retail Dataset reframed as commercial DD — segment economics, customer-base trajectory, concentration risk, LTV modeling, and post-close action planning. Built in R + Quarto, deployed on Netlify. Live report → https://lailara-retail-analysis.netlify.app/

### [data-hygiene-auditor](https://github.com/MsShawnP/data-hygiene-auditor)
Python CLI that audits Excel files for mixed formats, misused fields, placeholder floods, and phantom duplicates. Outputs HTML, Excel, and PDF reports.

### [field-story-scorer](https://github.com/MsShawnP/field-story-scorer)
Python CLI that scores every column in an Excel file across five data quality dimensions. Includes strict cell-level type detection that catches mixed-type columns pandas silently coerces.

### [gtin-validator](https://github.com/MsShawnP/gtin-validator)
Product data validation tool for specialty food brands preparing for national retail. Validates GTINs against GS1 standards with retailer-specific context (Walmart, Costco, UNFI, 1WorldSync), generates branded PDF reports, and includes a prioritized fix roadmap, case GTIN-14 generator, and product data completeness analysis. Deployed as a live Streamlit web app. Built in Python.

Try it live → https://msshawnp-gtin-validator-app-yz0mxn.streamlit.app/

### [product-data-audit-queries](https://github.com/MsShawnP/product-data-audit-queries)
SQL diagnostic queries for auditing product master data quality in specialty food and CPG companies preparing for national retail. 33 queries across 6 categories — GTIN/UPC validation, missing fields, data consistency, retailer readiness (Walmart, Costco, UNFI, Whole Foods), governance/staleness, and chargeback analysis. Built against a realistic fictional dataset (Cinderhaven Provisions). Built in SQL + Python.

---

## Background

**Current** — DDirector of Operations and Chief Solutions Architect at Incentive Insights (20+ years, still active). Principal Consultant, Lailara LLC.

**Prior** — Solution architect for the platform that became Incentive Insights. Before that, four years at TCA Fulfillment Services, staying on through its acquisition to help the new team get up to speed on the platform.

**Recent** — Contract work auditing data quality for large language model training — reviewing and scoring response batches against accuracy, formatting, and domain knowledge standards.

**Credentials** — HarvardX coursework in data science and Python/ML. Harvard Business School Online certificates in strategy execution and digital marketing strategy.

---

## Tools

Power BI, SQL, Python, R, Quarto, Crystal Reports, Excel (the serious kind), VS Code, Claude Code, Streamlit,Netlify

---

## How I Work

Fractional engagements only. Fixed-fee or monthly retainer. No timesheets, no hourly billing. I work on outcomes, not hours. Typical first engagement is a 4–6 week scoped audit with a written assessment and remediation plan. From there we decide whether an ongoing retainer makes sense.

---

## How To Start

A 30-minute scoping conversation. No obligation, no deck.

- **Email:** msshawnp@gmail.com
- **Phone:** 914-434-0932
- **LinkedIn:** [in/shawn-phillips-b383b3149](https://www.linkedin.com/in/shawn-phillips-b383b3149/)

