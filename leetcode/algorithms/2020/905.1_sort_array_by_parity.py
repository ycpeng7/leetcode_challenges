#-------------------------------------------------------------------------------
#    Sort Array By Parity
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/sort-array-by-parity/
# Completed 11/19/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Two-pointer
1. i from start, j from end
2. Once i meets an odd number, keep moving j until it's even
3. Swap num[i] and num[j]
4. Increment i and decrement j

Time: O(n)
Space: O(1)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def sort_array(lis: [int]):
    i, j = 0, len(lis) - 1
    while j > i:
        if lis[i] % 2 == 1:
            while lis[j] % 2 != 0 and j > i:
                j -= 1
            if j > i:
                lis[j], lis[i] = lis[i], lis[j]
        i += 1
    return lis            


#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def sortArrayByParity(self, A: [int]) -> [int]:
        return sort_array(A)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    def test_generic(self):
        nums = [3, 1, 2, 4]
        ans = [2, 4, 3, 1]
        self.assertCountEqual(Solution().sortArrayByParity(nums), ans)
    def test_generic_2(self):
        nums = [2, 4, 3, 1]
        ans = [2, 4, 3, 1]
        self.assertCountEqual(Solution().sortArrayByParity(nums), ans)
    def test_all_even(self):
        nums = [0, 2, 4, 6]
        ans = [0, 2, 4, 6]
        self.assertCountEqual(Solution().sortArrayByParity(nums), ans)
    def test_all_odds(self):
        nums = [1, 3, 5, 7]
        ans = [1, 3, 5, 7]
        self.assertCountEqual(Solution().sortArrayByParity(nums), ans)
    def test_empty(self):
        nums = []
        ans = []
        self.assertCountEqual(Solution().sortArrayByParity(nums), ans)
    def test_single_odd_element(self):
        nums = [1]
        ans = [1]
        self.assertCountEqual(Solution().sortArrayByParity(nums), ans)
    def test_single_even_element(self):
        nums = [2]
        ans = [2]
        self.assertCountEqual(Solution().sortArrayByParity(nums), ans)

if __name__ == '__main__':
    unittest.main()