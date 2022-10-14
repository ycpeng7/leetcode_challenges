#-------------------------------------------------------------------------------
#    Two Sum
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/two-sum/
# Completed 11/18/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Create a hashmap
2. For each element in nums, check if key exists, if yes, return indexes 
3. If not, create key as target - num and value as index
Time: O(n)
Space: O(n)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------


class TwoSum:
    def __init__(self, nums: [int], target: int):
        self.nums = nums
        self.target = target
    def solve(self):
        self.num_dict = {}
        for i in range(len(self.nums)):
            if self.num_dict.get(self.nums[i]) is not None:
                return [self.num_dict[self.nums[i]], i]
            else:
                self.num_dict[self.target - self.nums[i]] = i

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        return TwoSum(nums, target).solve()

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    def test_1_2_3(self):
        nums = [1, 2]
        target = 3
        ans = [0,1]
        self.assertEqual(Solution().twoSum(nums, target), ans)
    def test_1_1_2(self):
        nums = [1, 1]
        target = 2
        ans = [0,1]
        self.assertEqual(Solution().twoSum(nums, target), ans)        
    def test_many(self):
        nums = [1, 2, 30, 4, 5, 6, 7, 8, 9]
        target = 36
        ans = [2,5]
        self.assertEqual(Solution().twoSum(nums, target), ans)        
    def test_0_1_1(self):
        nums = [0, 2, 1]
        target = 1
        ans = [0,2]
        self.assertEqual(Solution().twoSum(nums, target), ans)        
    def test_example1(self):
        nums = [2, 7, 11, 15]
        target = 9
        ans = [0,1]
        self.assertEqual(Solution().twoSum(nums, target), ans)
    def test_dont_duplicate_index(self):
        nums = [3, 2, 4]
        target = 6
        ans = [1, 2]
        self.assertEqual(Solution().twoSum(nums, target), ans)
    def test_negative(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        ans = [2, 4]
        self.assertEqual(Solution().twoSum(nums, target), ans)
    def test_duplicate(self):
        nums = [1, 1, 2, 2, 3, 3, 7, 10]
        target = 17
        ans = [6, 7]
        self.assertEqual(Solution().twoSum(nums, target), ans)

if __name__ == '__main__':
    unittest.main()