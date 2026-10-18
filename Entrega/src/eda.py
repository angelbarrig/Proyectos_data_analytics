import pandas as pd

def describe_bank(df):
    return {
        "summary": df.describe(include='all'),
        "missing": df.isna().sum(),
        "correlation": df.corr(numeric_only=True)
    }

def describe_customer(dfs):
    return {name: df.describe(include='all') for name, df in dfs.items()}
