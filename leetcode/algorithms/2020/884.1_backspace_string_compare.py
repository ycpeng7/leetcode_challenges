#-------------------------------------------------------------------------------
#    Backspace String Compare
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/backspace-string-compare/
# Completed 11/24/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Pointer for each string starting from end
2. "#" skip + 1
3. Else skip - 1
4. If skip = 0, compare character from two lists
5. If same, both pointers move forward 

Time: 
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class Solution:

    def _get_next_index(self, string: str, index: int):
        skip = 0
        while index >= 0:
            if string[index] == '#':
                skip += 1
            else:
                if skip > 0:
                    skip -= 1
                else:
                    break
            index -= 1
        return index

    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        
        while True:
            i = self._get_next_index(S, i)
            j = self._get_next_index(T, j)
            if i == -1 and j == -1:
                return True
            elif (i == -1 and j != -1) or (j == -1 and i != -1) or S[i] != T[j]:
                return False
            i -= 1
            j -= 1

                        


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    def test_generic(self):
        S = "ab#c"
        T = "ad#c"
        ans = True
        self.assertEqual(Solution().backspaceCompare(S, T), ans)
    def test_generic_2(self):
        S = "###ab#c"
        T = "##ad#c"
        ans = True
        self.assertEqual(Solution().backspaceCompare(S, T), ans)
    def test_generic_3(self):
        S = "aab#c"
        T = "##ad#c"
        ans = False
        self.assertEqual(Solution().backspaceCompare(S, T), ans)

   

if __name__ == '__main__':
    unittest.main()