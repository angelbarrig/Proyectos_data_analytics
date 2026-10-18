import pandas as pd

def load_bank_data(path):
    return pd.read_csv(path, sep=',')

def load_customer_data(path):
    return pd.read_excel(path, sheet_name=None)
