#-------------------------------------------------------------------------------
#    Sum of All Odd Length Subarrays
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
# Completed 11/20/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Start with sub_len = 1
2. Find sum of all subarrays with sub_len
3. Increment sub_len by 2 until it's larger or equal to length of arr

Time: O(n^2)
Space: O(1)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def sum_array(arr: [int]):
    ans = 0
    sub_len = 1
    while sub_len <= len(arr):
        i = 0
        while i + sub_len - 1 < len(arr):
            ans += sum(arr[i: i + sub_len])
            i += 1
        sub_len += 2
    return ans
    
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def sumOddLengthSubarrays(self, arr: [int]) -> int:
        return sum_array(arr)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    def test_generic(self):
        arr = [1,4,2,5,3]
        ans = 58
        self.assertEqual(Solution().sumOddLengthSubarrays(arr), ans)
    def test_two_nums(self):
        arr = [1,2]
        ans = 3
        self.assertEqual(Solution().sumOddLengthSubarrays(arr), ans)
    def test_one_num(self):
        arr = [1]
        ans = 1
        self.assertEqual(Solution().sumOddLengthSubarrays(arr), ans)
    def test_empty_num(self):
        arr = []
        ans = 0
        self.assertEqual(Solution().sumOddLengthSubarrays(arr), ans)

if __name__ == '__main__':
    unittest.main()