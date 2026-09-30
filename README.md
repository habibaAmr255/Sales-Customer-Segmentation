# Online Retail: Customer Analytics & Segmentation

RFM analysis and K-Means customer segmentation on one year of transactions from a UK online retailer
(541,909 transaction lines, Dec 2010 - Dec 2011).

## Project structure

```
online-retail-segmentation/
├── data/
│   ├── Online Retail.xlsx        # raw data
│   ├── data_dictionary.md        # column descriptions + files created by the notebooks
│   ├── sales_clean.csv           # created by notebook 01
│   └── rfm.csv                   # created by notebook 03
├── notebooks/
│   ├── 01_cleaning.ipynb         # business understanding, audit, cleaning, feature engineering
│   ├── 02_eda.ipynb              # EDA and business insights
│   ├── 03_rfm.ipynb              # customer features, RFM scoring and visualization
│   └── 04_clustering.ipynb       # preprocessing, clustering, profiling, recommendations
├── src/
│   └── cleaning.py               # clean_data() and add_features() used by notebook 01
├── reports/
│   └── final_summary.pdf         # 2-page summary
├── requirements.txt
└── README.md
```

## How to run

```bash
pip install -r requirements.txt
cd notebooks
jupyter notebook
```

Run the notebooks **in order** (01 -> 04). Each notebook saves a file in `data/` that the next one reads.
`random_state=42` is used everywhere, so the results are reproducible.

## Main results

- Net revenue GBP 9.75M; returns are 8.4% of gross sales. The top 20% of products give about 79% of product revenue.
- The UK generates 84% of revenue; November 2011 is the peak month (GBP 1.46M).
- 4,317 customers were segmented with K-Means (K = 4) on log-transformed, standardized RFM:

| Segment | Customers | Revenue share |
|---|---|---|
| Champions | 16.1% | 64.7% |
| Mid-Value Regulars | 27.3% | 23.3% |
| New / Recent Low-Frequency | 19.2% | 5.5% |
| Lapsed Low-Value | 37.4% | 6.5% |

- A further 173 high-value customers stopped buying (GBP 382k of revenue) and are the main win-back target.

## Key decisions

- Cancellations are kept as negative revenue; duplicates and `UnitPrice <= 0` lines are removed.
- Lines without `CustomerID` (guest invoices) are kept for sales analysis and excluded from RFM.
- Monetary = net revenue (purchases minus returns); customers with zero or negative net revenue are excluded from RFM.
- `CustomerID` is an identifier only and is never used as a model feature.
