#-------------------------------------------------------------------------------
#    Maximum Subarray
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/maximum-subarray/
# Completed 11/19/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
DP Bottom Up, modify nums in-place
1. Loop through nums
2. Check if previous num (already modified) > 0
3. If yes, add previous num to current, if no, continue loop

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
        max_sum = self.nums[0]
        for i in range(1, len(self.nums)):
            if self.nums[i - 1] > 0:
                self.nums[i] += self.nums[i - 1]
            max_sum = max(max_sum, self.nums[i])
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