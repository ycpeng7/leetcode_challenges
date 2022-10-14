#-------------------------------------------------------------------------------
#    Merge Intervals
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/merge-intervals/
# Completed 12/15/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Sort
2. sliding window


Time: O(nlogn)
Space: O(1)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------


class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        intervals = sorted(intervals)
        i = 0
        res = []
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            j = i + 1
            while j < len(intervals) and intervals[j][0] <= end:
                end = max(end, intervals[j][1])
                j += 1
            i = j
            res.append([start, end])
        return res


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest


class TestSolution(unittest.TestCase):
    def test_generic(self):
        intervals = [[1,4],[4,5]]
        ans = [[1,5]]
        self.assertEqual(Solution().merge(intervals), ans)
    def test_generic2(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        ans = [[1,6],[8,10],[15,18]]
        self.assertEqual(Solution().merge(intervals), ans)
    def test_generic3(self):
        intervals = [[1,5],[8,10],[15,18]]
        ans = [[1,5],[8,10],[15,18]]
        self.assertEqual(Solution().merge(intervals), ans)


if __name__ == '__main__':
    unittest.main()