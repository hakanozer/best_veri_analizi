# services/service.py
import pandas as pd
import numpy as np


def load_data():
    df = pd.read_csv(
        "data/raw/planlama.csv",
        sep=";",
        encoding="latin-1",
        decimal=",",
        parse_dates=["Tarih"],
        dayfirst=True
    )
    return df


def tum_data_sayfalama(df: pd.DataFrame, page: int, size: int) -> dict:
    start = (page - 1) * size
    end = start + size

    data = df.iloc[start:end]
    
    data = data.replace([np.inf, -np.inf], np.nan).fillna(0)

    return {
        "page": page,
        "size": size,
        "total": len(df),
        "data": data.to_dict(orient="records")
    }
    
    
def guc_1000_max_12000(df: pd.DataFrame) -> pd.DataFrame: 
    ozet = df.head(100000).query("Guc > 1000").fillna(0).query("Guc < 1200") 
    return ozet