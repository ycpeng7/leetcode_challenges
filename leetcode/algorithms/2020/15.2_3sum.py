#-------------------------------------------------------------------------------
#    3Sum
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/3sum/
# Completed 12/5/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Sort the list first
2. For each element, apply two sum approach to all the elements to its right 


Time: O(n^2)
Space: O(1)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------


class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        res = []
        nums = sorted(nums)
        prev = float('inf')
        for i, num in enumerate(nums):
            if num == prev:
                continue
            if num > 0:
                break
            left = i + 1
            right = len(nums) - 1
            prev = num
            while left < right:
                if nums[left] + nums[right] == -num:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left <= right:
                        left += 1
                elif nums[left] + nums[right] < -num:
                    left += 1
                else:
                    right -= 1
        return res 


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest


class TestSolution(unittest.TestCase):
    def test_generic(self):
        nums = [-1,0,1,2,-1,-4]
        ans = [[-1,-1,2],[-1,0,1]]
        self.assertCountEqual(Solution().threeSum(nums), ans)
    def test_empty(self):
        nums = []
        ans = []
        self.assertCountEqual(Solution().threeSum(nums), ans)
    def test_zero(self):
        nums = [0]
        ans = []
        self.assertCountEqual(Solution().threeSum(nums), ans)
    def test_duplicate(self):
        nums = [-2,0,0,2,2]
        ans = [[-2,0,2]]
        self.assertCountEqual(Solution().threeSum(nums), ans)


if __name__ == '__main__':
    unittest.main()