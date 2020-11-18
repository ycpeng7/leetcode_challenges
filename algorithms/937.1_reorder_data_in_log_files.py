#-------------------------------------------------------------------------------
#    Reorder Data in Log Files
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/reorder-data-in-log-files/
# Completed 11/18/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Create another list for digit-logs, pop digit-log from original and apend to it
2. Sort the original list by words after the identifier
3. Append digit-log list to original list
Time: O(nlogn)
Space: O(n)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------


class ReorderDataInLogFiles:
    def __init__(self, logs: [str]):
        self.logs = logs
        self.digit_logs = []
    def _append_digit_logs(self):
        digit_index = []
        for i in range(len(self.logs)):
            try:
                int(self.logs[i].split(" ")[1])
                digit_index.append(i)
                self.digit_logs.append(self.logs[i])
            except ValueError:
                continue
        self.logs = [self.logs[i] for i in range(len(self.logs)) if i not in digit_index]
    def solve(self):
        self._append_digit_logs()
        if len(self.logs) == 0:
            return self.digit_logs
        else:
            self.logs = sorted(self.logs, key=lambda x:
                 (" ".join(x.split(" ")[1:]), x.split(" ")[0]))
            return self.logs + self.digit_logs

        
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def reorderLogFiles(self, logs: [str]) -> [str]:
        return ReorderDataInLogFiles(logs).solve()

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    def test_normal(self):
        logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        ans = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
        self.assertEqual(Solution().reorderLogFiles(logs), ans)
    def test_normal_tie_logs(self):
        logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","get2 art zero","aet3 art zero"]
        ans = ["let1 art can","aet3 art zero","get2 art zero","dig1 8 1 5 1","dig2 3 6"]
        self.assertEqual(Solution().reorderLogFiles(logs), ans)
    def test_no_letter_log(self):
        logs = ["dig1 8 1 5 1", "dig2 3 6"]
        ans = ["dig1 8 1 5 1", "dig2 3 6"]
        self.assertEqual(Solution().reorderLogFiles(logs), ans)
    def test_no_digit_log(self):
        logs = ["let1 art can","let2 own kit dig","let3 art zero"]
        ans = ["let1 art can", "let3 art zero", "let2 own kit dig"]
        self.assertEqual(Solution().reorderLogFiles(logs), ans)
    def test_empty_log(self):
        logs = []
        ans = []
        self.assertEqual(Solution().reorderLogFiles(logs), ans)
    
   

if __name__ == '__main__':
    unittest.main()