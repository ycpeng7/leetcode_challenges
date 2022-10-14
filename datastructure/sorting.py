import unittest
#-------------------------------------------------------------------------------
#    Implementation of common sorting algorithms
#-------------------------------------------------------------------------------


def selection_sort(lis: list[int]) -> list[int]:
    """
    Take the min of unsorted list and append to sorted list
    Avg: O(N^2)
    Best: O(N^2)
    Worst: O(N^2)
    """
    sorted_lis = lis
    for i in range(len(sorted_lis)):
        j = i + 1
        min_ind = i
        while (j < len(sorted_lis)):
            if sorted_lis[j] < sorted_lis[min_ind]:
                min_ind = j
            j += 1
        sorted_lis[i], sorted_lis[min_ind] = sorted_lis[min_ind], sorted_lis[i]
    return sorted_lis


def insertion_sort(lis: list[int]) -> list[int]:
    """
    Insert each element of unsorted list in the right location in sorted list
    Avg: O(N^2)
    Best: O(N)
    Worst: O(N^2)
    Twice as fast as bubble_sort, because of less comparisons
    """
    sorted_lis = lis
    for i in range(1, len(sorted_lis)):
        j = i
        while(j > 0 and sorted_lis[j] < sorted_lis[j - 1]):
            sorted_lis[j], sorted_lis[j - 1] = sorted_lis[j - 1], sorted_lis[j]
            j -= 1
    return sorted_lis


def bubble_sort(lis: list[int]) -> list[int]:
    """
    Start from beginning, if the right neighbor is smaller, swap, keep doing it till the end.
    Repeat N times. The largest number is moved the rightmost position each time. 
    Avg: O(N^2)
    Best: O(N)
    Worst: O(N^2)
    """
    sorted_lis = lis
    for i in range(len(sorted_lis)):
        swapped = False
        for j in range(1, len(sorted_lis)):
            if sorted_lis[j] < sorted_lis[j - 1]:
                sorted_lis[j], sorted_lis[j - 1] = sorted_lis[j - 1],  sorted_lis[j]
                swapped = True
        if not swapped:
            break
    return sorted_lis



class merge_sort():
    """
    1. Divide list into half
    2. Sort left
    3. Sort right
    4. Merge left and right
    Avg: O(NlogN)
    Best: O(NlogN)
    Worst: O(NlogN)
    """

    def _merge(self, left: list[int], right: list[int]) -> list[int]:
        merged_lis = []
        left_len, right_len = len(left), len(right)
        left_iter, right_iter = 0, 0
        while left_iter < left_len and right_iter < right_len:
            if left[left_iter] > right[right_iter]:
                merged_lis.append(right[right_iter])
                right_iter += 1
            else:
                merged_lis.append(left[left_iter])
                left_iter += 1
        for i in range(left_iter, left_len):
            merged_lis.append(left[i])
        for i in range(right_iter, right_len):
            merged_lis.append(right[i])
        return merged_lis

    def solve(self, lis: list[int]) -> list[int]:
        sorted_lis = lis
        n = len(sorted_lis)
        if n <= 1:
            return sorted_lis
        mid = n // 2
        left = self.solve(sorted_lis[0:mid])
        right = self.solve(sorted_lis[mid:n])
        return self._merge(left, right)


class quick_sort():
    """
    1. Choose the last element as pivot
    2. We want to put everything smaller to the left of pivot, greater to the right
    3. That means at the end, there's an index, first_larger, where everything to the left is smaller than pivot, and to the right is larger, including itself
    4. first_larger equals to start index, and when we see one smaller element, swap with lis[first_larger], and increment first_larger
    Avg: O(NlogN)
    Worst: O(N^2) - When the pivot is always the smallest or the largest
    Best: O(NlogN)
    """
    
    def _partition(self, start: int, end: int, lis: list[int]) -> int:
        pivot = lis[end]
        first_larger = start
        for i in range(start, end):
            if lis[i] < pivot:
                lis[first_larger], lis[i] = lis[i], lis[first_larger]
                first_larger += 1
        lis[first_larger], lis[end] = lis[end], lis[first_larger]
        return first_larger
    
    def _sort(self, lis: list[int], start: int, end: int):
        if start >= end:
            return
        ind = self._partition(start, end, lis)
        self._sort(lis, start, ind - 1)
        self._sort(lis, ind + 1, end)
    
    def solve(self, lis: list[int]) -> list[int]:
        self._sort(lis, 0, len(lis) - 1)   
        return lis    
        


class TestSorting(unittest.TestCase):
    def test_generic(self):
        lis = [9, 8, 1, 5]
        for sort in [bubble_sort, selection_sort, insertion_sort,
                     merge_sort().solve, quick_sort().solve]:
            self.assertEqual(sort(lis.copy()), sorted(lis))
    def test_single_element(self):
        lis = [0]
        for sort in [bubble_sort, selection_sort, insertion_sort,
                     merge_sort().solve, quick_sort().solve]:
            self.assertEqual(sort(lis.copy()), sorted(lis))
    def test_empty(self):
        lis = []
        for sort in [bubble_sort, selection_sort, insertion_sort,
                     merge_sort().solve, quick_sort().solve]:
            self.assertEqual(sort(lis.copy()), sorted(lis))
    def test_all_reversed(self):
        lis = [-x for x in range(500)]
        for sort in [bubble_sort, selection_sort, insertion_sort,
                     merge_sort().solve, quick_sort().solve]:
            self.assertEqual(sort(lis.copy()), sorted(lis))


if __name__ == "__main__":
    unittest.main()