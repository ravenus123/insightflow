from pathlib import Path
import pandas as pd
from app.core.exceptions import InvalidDatasetError


def read_csv_dataset(path: Path) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
    except Exception as exc:
        raise InvalidDatasetError("The CSV file could not be parsed.") from exc

    if df.empty:
        raise InvalidDatasetError("The dataset is empty.")
    if len(df.columns) == 0:
        raise InvalidDatasetError("The dataset has no columns.")
    return df
