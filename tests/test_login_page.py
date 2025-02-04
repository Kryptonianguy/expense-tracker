import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize("a, b, expected", [(45, 10, 55), (20, 5, 25)])
def test_add(a, b, expected):
    assert add(a, b) == expected