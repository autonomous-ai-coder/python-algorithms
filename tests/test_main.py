import pytest
from your_module import quicksort

@pytest.fixture
    def unsorted_list():
        """
        Fixture for providing a generic unsorted list for testing.
        """
        return [3, 6, 8, 10, 1, 2, 1]

@pytest.fixture
    def sorted_list():
        """
        Fixture for providing a sorted list for testing.
        """
        return [1, 1, 2, 3, 6, 8, 10]

class TestQuickSort:

    def test_basic_functionality(self, unsorted_list, sorted_list):
        """
        Test basic functionality of quicksort with a generic unsorted list.
        """
        assert quicksort(unsorted_list) == sorted_list

    def test_empty_list(self):
        """
        Test quicksort with an empty list.
        """
        assert quicksort([]) == []

    def test_single_element_list(self):
        """
        Test quicksort with a single element list.
        """
        assert quicksort([1]) == [1]

    def test_identical_elements(self):
        """
        Test quicksort with a list where all elements are the same.
        """
        assert quicksort([7, 7, 7, 7]) == [7, 7, 7, 7]

    def test_sorted_list(self, sorted_list):
        """
        Test quicksort with an already sorted list.
        """
        assert quicksort(sorted_list) == sorted_list

    def test_reverse_sorted_list(self):
        """
        Test quicksort with a reverse sorted list.
        """
        assert quicksort([10, 8, 6, 3, 2, 1, 1]) == [1, 1, 2, 3, 6, 8, 10]

    def test_large_numbers(self):
        """
        Test quicksort with a list of large numbers.
        """
        assert quicksort([1000000, 500000, 100000, 50000]) == [50000, 100000, 500000, 1000000]

    def test_negative_numbers(self):
        """
        Test quicksort with a list of negative numbers.
        """
        assert quicksort([-1, -3, -2, -5]) == [-5, -3, -2, -1]

    def test_mixed_numbers(self):
        """
        Test quicksort with a list of mixed positive and negative numbers.
        """
        assert quicksort([-1, 3, 2, -5, 0]) == [-5, -1, 0, 2, 3]

    def test_performance_large_list(self):
        """
        Performance test with a large list of random elements.
        """
        import random
        large_list = random.sample(range(1, 1000000), 10000)
        sorted_list = sorted(large_list)
        assert quicksort(large_list) == sorted_list

    def test_error_non_integer(self):
        """
        Test handling of non-integer elements in the list.
        """
        with pytest.raises(TypeError):
            quicksort([1, 'two', 3])
