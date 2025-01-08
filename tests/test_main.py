@pytest.fixture
def sorted_data():
    """
    Provides a fixture for a basic sorted dataset.
    """
    return [4, 5, 6, 7, 8]

@pytest.fixture
def unsorted_data():
    """
    Provides a fixture for a basic unsorted dataset.
    """
    return [8, 4, 6, 7, 5]

@pytest.fixture
def empty_data():
    """
    Provides a fixture for an empty dataset.
    """
    return []

@pytest.fixture
def large_data():
    """
    Provides a fixture for a large dataset.
    """
    return list(range(1000, 0, -1))

def test_basic_sorted(sorted_data):
    """
    Test quicksort with an already sorted list.
    """
    assert quicksort(sorted_data) == [4, 5, 6, 7, 8]


def test_basic_unsorted(unsorted_data):
    """
    Test quicksort with a basic unsorted list.
    """
    assert quicksort(unsorted_data) == [4, 5, 6, 7, 8]


def test_empty_list(empty_data):
    """
    Test quicksort with an empty list.
    """
    assert quicksort(empty_data) == []


def test_large_input_performance(large_data):
    """
    Test quicksort performance with a large list.
    """
    sorted_large_data = list(range(1, 1001))
    assert quicksort(large_data) == sorted_large_data


def test_single_element():
    """
    Test quicksort with a single element list.
    """
    assert quicksort([1]) == [1]


def test_identical_elements():
    """
    Test quicksort with a list of identical elements.
    """
    assert quicksort([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]