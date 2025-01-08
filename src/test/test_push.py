
def test_function():
    """A simple test function"""
    return "Hello, GitHub!"

def add_numbers(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

# Test cases
def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
