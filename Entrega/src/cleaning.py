import pandas as pd

def clean_bank(df):
    df.columns = df.columns.str.lower().str.replace('.', '_')
    df = df.replace("unknown", pd.NA)
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['duration'] = pd.to_numeric(df['duration'], errors='coerce')
    df = df.drop_duplicates()
    return df

def clean_customer(dfs):
    cleaned = {}
    for name, df in dfs.items():
        df.columns = df.columns.str.lower()
        df['dt_customer'] = pd.to_datetime(df['dt_customer'], errors='coerce')
        df = df.drop_duplicates()
        cleaned[name] = df
    return cleaned
