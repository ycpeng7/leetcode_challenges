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
2. Starting the 2nd word, append the occurences to the dictionary only if it
   already exists
3. In the end, return only those keys having same length of list, and get the minimum
   occurences

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
        first = A[0]
        occurences = {}
        for char in first:
            if occurences.get(char) is None:
                occurences[char] = [1]
            else:
                occurences[char][0] += 1
        for i in range(1, len(A)):
            for char in A[i]:
                if occurences.get(char) is None or len(occurences.get(char)) < i:
                    continue
                else:
                    if len(occurences[char]) == i + 1:
                        occurences[char][i] += 1
                    else:
                        occurences[char].append(1)
        ans = []
        for char in occurences:
            if len(occurences[char]) == len(A):
                for _ in range(min(occurences[char])):
                    ans.append(char)
        return ans


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