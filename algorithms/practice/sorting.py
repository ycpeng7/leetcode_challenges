import unittest
#-------------------------------------------------------------------------------
#    Implementation of common sorting algorithms
#-------------------------------------------------------------------------------


def bubble_sort(lis):
    """
    Put the largest element to the rightmost position each time
    1. Set done flag = True
    2. Start with i = 0, swap i and i + 1 if num[i] > num[i + 1]
    3. done = False if any swap occured
    4. Keep running while done is False
    """
    j = 0
    done = False
    while not done:
        done = True
        for i in range(len(lis) - j - 1):
            if lis[i] > lis[i + 1]:
                lis[i], lis[i + 1] = lis[i + 1], lis[i]
                done = False
        j += 1
    return lis


def selection_sort(lis):
    """
    Take the min of unsorted list and append to sorted list
    """
    for i in range(len(lis)):
        min_ind = i
        for j in range(i + 1, len(lis)):
            if lis[j] < lis[min_ind]:
                min_ind = j
        lis[i], lis[min_ind] = lis[min_ind], lis[i]
    return lis


def insertion_sort(lis):
    """
    Insert each element of unsorted list in the right location in sorted list
    """
    for i in range(1, len(lis)):
        j = i
        while lis[j] < lis[j - 1] and j > 0:
            lis[j], lis[j - 1] = lis[j - 1], lis[j]
            j -= 1
    return lis


class merge_sort():
    """
    1. Divide list into half
    2. Sort left
    3. Sort right
    4. Merge left and right
    """
    def _merge(self, left, right):
        merged = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged
                
    def solve(self, lis):
        if len(lis) <= 1:
            return lis
        mid = len(lis) // 2
        left = self.solve(lis[0: mid])
        right = self.solve(lis[mid: len(lis)])
        return self._merge(left, right)


class quick_sort():
    """
    1. Set last element as the pivot
    2. All those less than pivot goes to left
    3. All those larger goes to right
    """
    def _partition(self, lis, start: int, end: int):
        pivot = lis[end]
        j = start
        for i in range(start, end):
            if lis[i] < pivot:
                lis[i], lis[j] = lis[j], lis[i]
                j += 1
        lis[j], lis[end] = lis[end], lis[j]
        return j
    
    def _sort(self, lis, start: int, end: int):
        if start < end:
            pivot_ind = self._partition(lis, start, end)
            print(lis)
            self._sort(lis, start, pivot_ind - 1)
            self._sort(lis, pivot_ind + 1, end)

    def solve(self, lis):
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