#-------------------------------------------------------------------------------
#    Maximum Subarray
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/maximum-subarray/
# Completed 11/18/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Greedy
1. Loop through list
2. Keep updating the local max and global max

Time: O(n)
Space: O(1)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------


class MaximumSubarray:
    def __init__(self, nums: [int]):
        self.nums = nums
    def solve(self):
        max_sum = cur_sum = self.nums[0]
        for i in range(1, len(self.nums)):
            cur_sum = max(cur_sum + self.nums[i], self.nums[i])
            max_sum = max(cur_sum, max_sum)
        return max_sum


#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        return MaximumSubarray(nums).solve()

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    def test_normal(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        ans = 6
        self.assertEqual(Solution().maxSubArray(nums), ans)
    def test_all_negative(self):
        nums = [-2, -5, -1, -6]
        ans = -1
        self.assertEqual(Solution().maxSubArray(nums), ans)

   

if __name__ == '__main__':
    unittest.main()