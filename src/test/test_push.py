
import pytest

def add_numbers(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@pytest.fixture
def test_numbers():
    return [(1, 2, 3), (-1, 1, 0), (0, 0, 0)]

def test_add_numbers(test_numbers):
    """Test the add_numbers function with various inputs"""
    for a, b, expected in test_numbers:
        assert add_numbers(a, b) == expected
