#-------------------------------------------------------------------------------
#    Longest Palindromic Substring
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/longest-palindromic-substring/
# Completed 11/20/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. For each char, check even palindromes expanding from it, both to left and right,
   stop when not palindrome
2. Check the odd palindromes, stop when not palindrome
3. Move on to next Char

Time: O(n^2)
Space: O(1)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def expand_palindrome(s: str, max_substr: str, start: int, end: int):
    while start >= 0 and end < len(s) and s[start] == s[end]:
        if len(s[start: end + 1]) > len(max_substr):
            max_substr = s[start: end + 1]
        start -= 1
        end += 1
    return max_substr

def find_longest_palindrome(s: str):
    max_substr = s[0]
    for i in range(len(s)):
        # Check even palindromes
        max_substr = expand_palindrome(s, max_substr, i, i + 1)
        # Check odd palindromes
        max_substr = expand_palindrome(s, max_substr, i, i)
    return max_substr
        

        
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:            
    def longestPalindrome(self, s: str) -> str:
        return find_longest_palindrome(s)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    def test_generic(self):
        s = "badabaddb"
        ans = "badab"
        self.assertEqual(Solution().longestPalindrome(s), ans)
    def test_single(self):
        s = "bcdef"
        ans = "b"
        self.assertEqual(Solution().longestPalindrome(s), ans)
    def test_generic_2(self):
        s = "bddef"
        ans = "dd"
        self.assertEqual(Solution().longestPalindrome(s), ans)
    def test_full_str(self):
        s = "bdddb"
        ans = "bdddb"
        self.assertEqual(Solution().longestPalindrome(s), ans)

if __name__ == '__main__':
    unittest.main()