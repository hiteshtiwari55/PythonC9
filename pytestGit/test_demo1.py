
import pytest

def test_first_entry(test_setup):
    print("Before Conftest")
    print(test_setup)
#@pytest.fixture
def test_order():
    print("After Conftest")




