#-------------------------------------------------------------------------------
#    Find Common Characters
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/find-common-characters/
# Completed 11/23/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Create a dictionary that counts occurences of first word in the list
2. 

Time: O(n * m)
Space: O(n * m)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class Solution:
    def commonChars(self, A: [str]) -> [str]:
        if len(A) == 0:
            return []
        check = list(A[0])
        for word in A[1:]:
            new_check = []
            for char in word:
                if char in check:
                    # Remove first occurence of char
                    check.remove(char)
                    new_check.append(char)
            check = new_check
        return check


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    def test_generic(self):
        lis = ["bella","label","roller"]
        ans = ["e", "l", "l"]
        self.assertEqual(Solution().commonChars(lis), ans)
    def test_generic_2(self):
        lis = ["cool","lock","cook"]
        ans = ["c", "o"]
        self.assertEqual(Solution().commonChars(lis), ans)
    def test_no_common(self):
        lis = ["cool","abcd", "abdo"]
        ans = []
        self.assertEqual(Solution().commonChars(lis), ans)
   

if __name__ == '__main__':
    unittest.main()