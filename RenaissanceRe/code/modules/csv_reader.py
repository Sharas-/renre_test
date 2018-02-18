import pandas as pd

def read(csv_file):
    df = pd.read_csv(csv_file)
    return (df.columns.values.tolist(), df.values.tolist())
