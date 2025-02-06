# tests/test_core.py
import pytest
from calculator.core import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(2.5, 3.5) == 6.0

if __name__ == "__main__":
    pytest.main()