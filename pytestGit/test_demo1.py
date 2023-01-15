
import pytest
import pandas as pd
# sample Test
def test_first_entry(test_setup):
    print("Before Conftest")
    print(test_setup)
#@pytest.fixture
def test_order():
    print("After Conftest")
    print(pd.__version__)
    df = pd.DataFrame(range(0, 5))
    print("Hello!! Git crash course")
    print(df)




