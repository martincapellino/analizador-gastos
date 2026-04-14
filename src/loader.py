import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)
    df["fecha"] = pd.to_datetime(df["fecha"])
    return df
