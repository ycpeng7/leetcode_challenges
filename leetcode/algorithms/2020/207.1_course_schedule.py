#-------------------------------------------------------------------------------
#    Course Schedule
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/course-schedule/
# Completed 11/24/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Form directed graph from prerequisites
2. set visited as 0
3. For each course, find if there's any cycle, if yes return False
4. -1 means it's already visited in this cycle, 1 means this path works, no need to re-examine
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class Solution:      
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])
        visited = [[0] for _ in range(numCourses)]

        def dfs(start):
            if visited[start] == -1:
                return False
            elif visited[start] == 1:
                return True
            else:
                visited[start] = -1
                for neighbor in graph[start]:
                    if not dfs(neighbor):
                        return False
                visited[start] = 1
                return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True        
        



#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    def test_generic(self):
        num = 2
        prereq = [[0, 1]]
        ans = True
        self.assertEqual(Solution().canFinish(num, prereq), ans)
    def test_false(self):
        num = 2
        prereq = [[0, 1], [1, 0]]
        ans = False
        self.assertEqual(Solution().canFinish(num, prereq), ans)
    def test_generic_2(self):
        num = 5
        prereq = [[0, 1], [2, 1], [3, 0], [4, 2]]
        ans = True
        self.assertEqual(Solution().canFinish(num, prereq), ans)
   

if __name__ == '__main__':
    unittest.main()