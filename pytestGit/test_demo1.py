
import pytest
import pandas as pd

def test_first_entry(test_setup):
    print("Before Conftest")
    print(test_setup)
#@pytest.fixture
def test_order():
    print("After Conftest")
    df = pd.DataFrame(range(0, 5))
    print(df)




