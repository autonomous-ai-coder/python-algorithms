@pytest.fixture
def small_unsorted_list():
    """Fixture for a small unsorted list of integers."""
    return [3, 6, 8, 10, 1, 2, 1]

@pytest.fixture
def empty_list():
    """Fixture for an empty list."""
    return []

@pytest.fixture
def large_unsorted_list():
    """Fixture for a large list of integers."""
    return list(range(10000, 0, -1))

def test_basic_functionality(small_unsorted_list):
    """Test quicksort with a basic unsorted list."""
    result = quicksort(small_unsorted_list)
    assert result == sorted(small_unsorted_list)

def test_empty_list(empty_list):
    """Test quicksort with an empty list."""
    result = quicksort(empty_list)
    assert result == []

def test_large_input(large_unsorted_list):
    """Test quicksort with a large unsorted list for performance."""
    result = quicksort(large_unsorted_list)
    assert result == sorted(large_unsorted_list)

def test_single_element():
    """Test quicksort with a single element list."""
    result = quicksort([42])
    assert result == [42]

def test_identical_elements():
    """Test quicksort with all elements identical."""
    result = quicksort([5, 5, 5, 5, 5])
    assert result == [5, 5, 5, 5, 5]