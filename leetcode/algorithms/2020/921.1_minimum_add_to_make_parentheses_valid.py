#-------------------------------------------------------------------------------
#    Minimum Add to Make Parentheses Valid
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# Completed 11/23/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Push '(' to a stack
2. Count the number of times that there's no '(' in stack when ')' is encountered
3. Count the number of remaining '(' in the end
4. Add 2 and 3

Time: O(n)
Space: O(n)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        num_to_add = 0
        for string in S:
            if string == '(':
                stack.append(string)
            else:
                if len(stack) == 0:
                    num_to_add += 1
                else:
                    stack.pop()
        return num_to_add + len(stack)


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    def test_generic(self):
        S = '())'
        ans = 1
        self.assertEqual(Solution().minAddToMakeValid(S), ans)
    def test_generic_2(self):
        S = ')))((('
        ans = 6
        self.assertEqual(Solution().minAddToMakeValid(S), ans)
    def test_single_open(self):
        S = '('
        ans = 1
        self.assertEqual(Solution().minAddToMakeValid(S), ans)
    def test_single_close(self):
        S = ')'
        ans = 1
        self.assertEqual(Solution().minAddToMakeValid(S), ans)
    def test_no_add(self):
        S = '()'
        ans = 0
        self.assertEqual(Solution().minAddToMakeValid(S), ans)
    def test_empty(self):
        S = ''
        ans = 0
        self.assertEqual(Solution().minAddToMakeValid(S), ans)

if __name__ == '__main__':
    unittest.main()