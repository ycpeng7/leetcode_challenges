#-------------------------------------------------------------------------------
#    Longest Substring Without Repeating Characters
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Completed 11/20/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Maintain a dict of {"char": "position"}
2. When encounter a new character or if position is smaller than start,
   calculate length of substr
3. Else set start as dic[char] + 1
4. Update new position of character as dict[char]

Time: O(n)
Space: O(1) 
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def find_longest_substring(s: str):
    ans = 0
    char_position = {}
    start = 0
    for i in range(len(s)):
        if char_position.get(s[i]) is None or char_position.get(s[i]) < start:
            ans = max(ans, i - start + 1)
        else:
            start = char_position[s[i]] + 1
        char_position[s[i]] = i
    return ans
        
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return find_longest_substring(s)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    def test_generic(self):
        s = "badabaddb"
        ans = 3
        self.assertEqual(Solution().lengthOfLongestSubstring(s), ans)
    def test_single(self):
        s = "bcdef"
        ans = 5
        self.assertEqual(Solution().lengthOfLongestSubstring(s), ans)
    def test_generic_2(self):
        s = "bddef"
        ans = 3
        self.assertEqual(Solution().lengthOfLongestSubstring(s), ans)
    def test_full_str(self):
        s = "bbddb"
        ans = 2
        self.assertEqual(Solution().lengthOfLongestSubstring(s), ans)

if __name__ == '__main__':
    unittest.main()