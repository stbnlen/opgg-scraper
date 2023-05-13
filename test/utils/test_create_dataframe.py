import pytest
import pandas as pd
from utils.create_dataframe import create_dataframe

@pytest.fixture
def sample_data():
    return {
        'column1': [1, 2, 3],
        'column2': ['a', 'b', 'c']
    }

def test_create_dataframe_with_valid_data(sample_data):
    df = create_dataframe(sample_data)
    assert isinstance(df, pd.DataFrame)

def test_create_dataframe_with_invalid_data_type():
    with pytest.raises(TypeError):
        create_dataframe("invalid_data")

def test_create_dataframe_with_invalid_data():
    invalid_data = {
        'column1': [1, 2, 3],
        'column2': [4, 5]  # Different number of elements
    }
    with pytest.raises(ValueError):
        create_dataframe(invalid_data)
