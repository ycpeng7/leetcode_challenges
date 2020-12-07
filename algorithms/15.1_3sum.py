#-------------------------------------------------------------------------------
#    3Sum
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/3sum/
# Completed 12/4/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. For each element, solve it as a two-sum problem


Time: O(n^2)
Space: O(n)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------


class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        res = []
        dic = {}
        for i, num in enumerate(nums):
            if dic.get(num) is not None:
                continue
            dic[num] = {}
            target = -num
            for j in range(len(nums)):
                if j != i:
                    if dic[num].get(nums[j]) is True:
                        to_append = sorted([num, nums[j], target - nums[j]])
                        if to_append not in res:
                            res.append(to_append)
                        dic[num][nums[j]] = False
                    dic[num][target - nums[j]] = True
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

if __name__ == '__main__':
    unittest.main()