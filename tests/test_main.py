@pytest.fixture
def sample_data():
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

def test_basic_functionality(sample_data):
    """
    Test quicksort with a basic list of integers.
    """
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert quicksort(sample_data) == expected

@pytest.fixture
def empty_data():
    return []

def test_empty_input(empty_data):
    """
    Test quicksort with an empty list.
    """
    assert quicksort(empty_data) == []

@pytest.fixture
def large_data():
    return list(range(10000, 0, -1))

def test_large_input(large_data):
    """
    Test quicksort with a large input list to check performance.
    """
    expected = list(range(1, 10001))
    assert quicksort(large_data) == expected

def test_single_element():
    """
    Test quicksort with a single element list.
    """
    assert quicksort([1]) == [1]

def test_duplicate_elements():
    """
    Test quicksort with all elements the same.
    """
    assert quicksort([7, 7, 7, 7]) == [7, 7, 7, 7]

def test_already_sorted():
    """
    Test quicksort with an already sorted list.
    """
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]