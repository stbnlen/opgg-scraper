import pandas as pd
from typing import Dict, Any, Optional


def create_dataframe(data: Dict[str, Any]) -> Optional[pd.DataFrame]:
    """
    Creates a pandas DataFrame from a dictionary.

    Args:
        data: A dictionary containing the data to be converted to a DataFrame.

    Returns:
        A pandas DataFrame.

    Raises:
        ValueError: If the input data is not a valid input for creating a DataFrame.
        TypeError: If the input data is not a valid input for creating a DataFrame.
    """
    if not isinstance(data, dict):
        raise TypeError("Input data must be a dictionary.")
    return pd.DataFrame(data=data)
