from pathlib import Path
import pandas as pd
from app.core.exceptions import InvalidDatasetError

def read_dataset(path: Path) -> pd.DataFrame:
    try:
        if path.suffix.lower() == ".csv":
            df = pd.read_csv(path)
        elif path.suffix.lower() in {".xlsx", ".xlsm"}:
            df = pd.read_excel(path, engine="openpyxl")
        else:
            raise InvalidDatasetError("Unsupported dataset format.")
    except InvalidDatasetError:
        raise
    except Exception as exc:
        raise InvalidDatasetError("The dataset could not be parsed. Check the file format and headers.") from exc
    if df.empty:
        raise InvalidDatasetError("The dataset is empty.")
    if len(df.columns) == 0:
        raise InvalidDatasetError("The dataset has no columns.")
    df.columns = [str(c).strip() for c in df.columns]
    return df

# Backwards-compatible name used by older tests.
def read_csv_dataset(path: Path) -> pd.DataFrame:
    return read_dataset(path)
