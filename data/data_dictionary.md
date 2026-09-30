# Data Dictionary - Online Retail

Source: public *Online Retail* dataset (UK online retailer, 01 Dec 2010 - 09 Dec 2011).
File: `Online Retail.xlsx` (541,909 rows, 8 columns). One row = one transaction **line**.

| Column | Meaning |
|---|---|
| `InvoiceNo` | Invoice number. Starts with `C` for cancellations/returns |
| `StockCode` | Product code (5-digit = product; letters such as POST, DOT, M, AMAZONFEE = services/fees) |
| `Description` | Product name |
| `Quantity` | Units on the line (negative for returns) |
| `InvoiceDate` | Date and time of the invoice |
| `UnitPrice` | Price per unit (GBP) |
| `CustomerID` | Customer identifier (a label, not a numeric feature; missing for guest invoices) |
| `Country` | Customer country |

## Files created by the notebooks

| File | Created by | Content |
|---|---|---|
| `sales_clean.csv` | `01_cleaning.ipynb` | Cleaned lines + `TotalLineRevenue`, `Year`, `Month`, `DayOfWeek`, `Hour`, `Is_UK` |
| `rfm.csv` | `03_rfm.ipynb` | One row per customer: Recency, Frequency, Monetary, R/F/M scores, RFM_Score, CustomerAge |
