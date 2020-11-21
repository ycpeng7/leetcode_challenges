#-------------------------------------------------------------------------------
#    Product of Array Except Self
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/product-of-array-except-self/
# Completed 11/20/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Build the left_product array
2. Build the right_product array
3. For each num, times left_product and right_product

Time: O(n)
Space: O(n)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def product_array(arr: [int]):
    n = len(arr)
    left = [1] * n
    right = [1] * n
    for i in range(1, n):
        left[i] = left[i - 1] * arr[i - 1]
        right[n - i - 1] = right[n - i] * arr[n - i]
    return [left[i] * right[i] for i in range(n)]

    
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        return product_array(nums)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    def test_generic(self):
        arr = [1,2,3,4]
        ans = [24,12,8,6]
        self.assertEqual(Solution().productExceptSelf(arr), ans)
    def test_generic_2(self):
        arr = [5,8,10]
        ans = [80,50,40]
        self.assertEqual(Solution().productExceptSelf(arr), ans)
    def test_all_zero(self):
        arr = [0, 0]
        ans = [0, 0]
        self.assertEqual(Solution().productExceptSelf(arr), ans)
    def test_one_zero(self):
        arr = [0, 1]
        ans = [1, 0]
        self.assertEqual(Solution().productExceptSelf(arr), ans)

if __name__ == '__main__':
    unittest.main()