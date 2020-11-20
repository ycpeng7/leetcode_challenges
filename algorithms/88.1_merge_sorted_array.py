#-------------------------------------------------------------------------------
#    Merge Sorted Array
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/merge-sorted-array/
# Completed 11/19/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Two-pointer
1. Start from the end of lists, i for nums1, j for nums2
2. Compare nums1[i] and nums2[j], the larger one as nums1[m + n - k]

Time: O(n)
Space: O(1)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def merge_array(nums1: [int], m: int, nums2: [int], n: int):
    i, j, k = m - 1, n - 1, 1 
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[m + n - k] = nums1[i]
            i -= 1
        else:
            nums1[m + n - k] = nums2[j]
            j -= 1
        k += 1
    while j >= 0:
        nums1[j] = nums2[j]
        j -= 1
    


#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merge_array(nums1, m, nums2, n)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    def test_generic(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        ans = [1, 2, 2, 3, 5, 6]
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, ans)
    def test_empty_nums2(self):
        nums1 = [1, 2 ,3]
        m = 3
        nums2 = []
        n = 0
        ans = [1, 2, 3]
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, ans)
    def test_empty_nums1(self):
        nums1 = [0, 0]
        m = 0
        nums2 = [1, 2]
        n = 2
        ans = [1, 2]
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, ans)
    def test_both_empty(self):
        nums1 = []
        m = 0
        nums2 = []
        n = 0
        ans = []
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, ans)
    

if __name__ == '__main__':
    unittest.main()