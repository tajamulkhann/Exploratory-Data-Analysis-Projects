# Retail Sales and Profitability

Which categories generate revenue without healthy margins?

## Overview

A retailer sees growing sales but cannot tell whether discounts are eroding contribution. This beginner portfolio case study contains an original dataset, executable Python and SQL, a notebook with saved outputs and an offline dashboard. It is designed for learning, portfolio development and interview practice.

**Data status:** Synthetic. **Observation period:** Fictional 2025. **Author:** Tajamul Khan.

## Problem statement

- **Business question:** Which categories generate revenue without healthy margins?
- **Task:** Reconcile net sales and contribution across categories, regions and months.
- **Skills demonstrated:** Data cleaning · weighted margins · monthly trends.
- **Decision supported:** Prioritize an investigation or controlled test using reproducible evidence.

## STAR case study

### Situation
A retailer sees growing sales but cannot tell whether discounts are eroding contribution.

### Task
Reconcile net sales and contribution across categories, regions and months.

### Action
Deduplicate order lines, calculate net sales after discounts and returns, compare weighted contribution margins and reconcile SQL to Python. The workflow includes source profiling, explicit metric definitions, Python calculations, SQL checks and a documented handoff.

### Result
The executed analysis produced Net sales (USD): 1,924,136.3325; Contribution margin (%): 25.4698; Return rate (%): 7.3167. The notebook also exports a group-level summary and an SQL reconciliation. These are measured analytical outputs from synthetic data; no operational improvement has been demonstrated.

## Dataset

- **Availability:** Included at [`data/raw.csv`](data/raw.csv).
- **Source:** Original simulation in [`generate_data.py`](generate_data.py), seed `202600`.
- **Dictionary and grain:** [`data/README.md`](data/README.md).
- **License:** Included synthetic data is CC0-1.0; code is MIT licensed.
- No external data download, credentials or personal records are required.
- Simulated relationships are teaching assumptions, not facts about an industry.

## KPI definitions and analytical decisions

One row per order line; net_sales = quantity × price × (1 − discount) × (1 − returned); contribution subtracts retained-item cost; margin = sum(contribution) / sum(net_sales). Full returns have zero revenue and recover all inventory cost; reverse logistics is excluded.

Deduplicate order lines, calculate net sales after discounts and returns, compare weighted contribution margins and reconcile SQL to Python.

## Project workflow

1. Read the source and inspect its grain, missing values and duplicates.
2. Validate the data contract and handle fields according to their business meaning.
3. Calculate the defined metrics and segment-level summaries.
4. Run SQLite aggregation and reconcile shared measures against Python.
5. Generate the chart, CSV exports and standalone HTML dashboard.
6. Interpret the evidence, document limits and propose a next validation step.

## Verified results

The notebook was executed against the included dataset with an isolated in-process IPython session. Tables, printed checks and chart outputs remain embedded in the notebook.

| Metric | Executed value |
|---|---:|
| Net sales (USD) | 1,924,136.3325 |
| Contribution margin (%) | 25.4698 |
| Return rate (%) | 7.3167 |

These values describe this synthetic dataset and dependency environment. They are a reproducibility record, not a production benchmark or a causal effect unless explicitly defined in the randomized experiment.

![Analysis overview](outputs/overview.png)

## Evidence-based recommendation

The 30% discount band has the lowest observed contribution margin (7.33%). Investigate category mix before changing discount policy.

![Supporting analysis](outputs/detail.png)

The notebook contains the supporting breakdown in `outputs/detail.csv`. This recommendation is an investigation or validation step, not a claim of achieved impact.

## Dashboard and output files

Download or clone the project and open [`outputs/dashboard.html`](outputs/dashboard.html) in a browser. It works offline and provides KPI cards, a chart and a searchable summary table. The text filter only filters table rows; it does not recompute cards or charts. GitHub's file view does not execute HTML dashboards.

| File | Purpose |
|---|---|
| [`analysis.ipynb`](analysis.ipynb) | Narrative analysis with executed code, tables and chart |
| [`analysis.py`](analysis.py) | Script companion with the same analysis code |
| [`analysis.sql`](analysis.sql) | SQLite aggregation over validated `facts` |
| [`outputs/metrics.json`](outputs/metrics.json) | Machine-readable verified KPIs |
| [`outputs/summary.csv`](outputs/summary.csv) | Group-level analysis for Excel or BI tools |
| [`outputs/analysis_ready.csv`](outputs/analysis_ready.csv) | Validated analysis facts |
| [`outputs/sql_results.csv`](outputs/sql_results.csv) | SQL query results |
| [`outputs/data_quality.csv`](outputs/data_quality.csv) | Source profiling evidence |

## How to run

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
cd data-analytics/01-retail-sales-profitability
python -m jupyterlab analysis.ipynb
```

Run notebook cells from top to bottom. To execute as a script from the project directory:

```bash
python analysis.py
```

To rebuild the original dataset:

```bash
python generate_data.py
```

From the repository root, execute all notebooks and save their real outputs:

```bash
python scripts/execute_all.py
```

## Power BI / Tableau extension

Import `outputs/analysis_ready.csv` and `outputs/summary.csv`. Rebuild the specified measures with ratio-of-sums where relevant, add segment filters and reconcile the unfiltered totals to `outputs/metrics.json`. This package includes an HTML dashboard, not a PBIX or Tableau workbook.

## Limitations

Contribution excludes fixed overhead and tax. Discount comparisons are observational and do not establish causation.

## Recommended next step

Join actual campaign assignments and test a discount policy on a randomized holdout.

## Interview preparation

- What decision does this analysis support and what is the unit of analysis?
- Why did you choose this denominator and how could another denominator mislead?
- What did the data checks and SQL reconciliation establish?
- Which finding would you investigate first and what evidence would change your recommendation?
- What does this dataset prevent you from concluding?

### Resume bullet template

“Built a reproducible retail sales and profitability portfolio case study using Python and SQL, validated business metrics and delivered an offline dashboard with documented findings and limitations.”

Use this only after completing and understanding the project. Add a verified analysis metric if useful; do not describe simulated results as employer impact or claim an unmeasured percentage improvement.

### 60-second STAR answer

“In this simulated case study, a retailer sees growing sales but cannot tell whether discounts are eroding contribution. My task was to reconcile net sales and contribution across categories, regions and months. I used Python and SQL to validate the source, calculate defined metrics and communicate the results through a dashboard. The resulting metrics are recorded above. I would next join actual campaign assignments and test a discount policy on a randomized holdout.”

## Technologies

Python, Pandas, NumPy, SQLite, Matplotlib, Jupyter and HTML. The A/B testing project additionally uses SciPy.

## Author

**Tajamul Khan**

[GitHub](https://github.com/tajamulkhann) · [LinkedIn](https://www.linkedin.com/in/tajamulkhann/) · [Instagram](https://www.instagram.com/tajamul.codes/) · [Mentorship](https://topmate.io/tajamulkhan)

## Let's Connect

<div align="center">
<a href="https://www.linkedin.com/in/tajamulkhann/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
<a href="https://www.instagram.com/tajamul.codes/"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a>
<a href="https://topmate.io/tajamulkhan"><img src="https://img.shields.io/badge/Topmate-FF0000?style=for-the-badge"></a>
<a href="https://www.whatsapp.com/channel/0029VaYs05jJkK7JKCesw42f"><img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white"></a>
<a href="https://t.me/tajamul_khan"><img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white"></a>
<a href="https://substack.com/@tajamulkhan"><img src="https://img.shields.io/badge/Substack-FF6719?style=for-the-badge&logo=substack&logoColor=white"></a>
<a href="https://www.kaggle.com/tajamulkhan"><img src="https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white"></a>
<a href="https://github.com/tajamulkhann"><img src="https://img.shields.io/badge/GitHub-12100E?style=for-the-badge&logo=github&logoColor=white"></a>
<a href="https://medium.com/@tajamulkhan"><img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white"></a>
</div>

