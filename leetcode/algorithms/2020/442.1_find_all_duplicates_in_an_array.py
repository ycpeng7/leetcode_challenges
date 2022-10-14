#-------------------------------------------------------------------------------
#    Find All Duplicates in an Array
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Completed 11/23/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Since 1 <= a[i] <= n, negate a[abs(a[i]) - 1] at i th element
2. If it's already negated, means duplicate

Time: O(n)
Space: O(1)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class Solution:
    def findDuplicates(self, nums: [int]) -> [int]:
        ans = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                ans.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] *= -1
        return ans
                


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    def test_generic(self):
        lis = [4,3,2,7,8,2,3,1]
        ans = [2,3]
        self.assertEqual(Solution().findDuplicates(lis), ans)

   

if __name__ == '__main__':
    unittest.main()