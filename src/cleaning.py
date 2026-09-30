"""Reusable cleaning functions for the Online Retail project.

Used by notebooks/01_cleaning.ipynb. Each step is explained (with its
business impact) in that notebook.
"""
import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove exact duplicate lines and keep only lines with UnitPrice > 0.

    - Exact duplicates would double-count sales.
    - UnitPrice <= 0 lines are accounting adjustments / stock write-offs, not sales.
    - Cancellations (negative quantity) and missing CustomerID are KEPT here:
      returns reduce net revenue, and guest invoices are real revenue.
    """
    df = df.drop_duplicates()
    return df[df['UnitPrice'] > 0].copy()


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add revenue, calendar and geography features."""
    df = df.copy()
    df['TotalLineRevenue'] = df['Quantity'] * df['UnitPrice']   # negative for returns

    df['Year'] = df['InvoiceDate'].dt.year
    df['Month'] = df['InvoiceDate'].dt.month
    df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek            # 0 = Monday
    df['Hour'] = df['InvoiceDate'].dt.hour

    df['Is_UK'] = (df['Country'] == 'United Kingdom').astype(int)
    return df
