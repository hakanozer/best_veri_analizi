from pathlib import Path
import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(path)


def save_df(df: pd.DataFrame, path: str) -> None:
    """Save a DataFrame to CSV, creating parent dirs as needed."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
