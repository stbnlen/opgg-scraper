import pandas as pd
from typing import Dict


def create_dataframe(objects: Dict[str, any]) -> pd.DataFrame:
    try:
        df = pd.DataFrame(objects)
        df.index = range(len(df))
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
