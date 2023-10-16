import pandas as pd

def ReadCsvModel(name, folder):
    if name is None:
        return None
    
    if folder is None:
        return pd.read_csv(name)
    
    return pd.read_csv(f'datasets/{folder}/{name}.csv')

