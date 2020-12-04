#-------------------------------------------------------------------------------
#    Evaluate Division
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/evaluate-division/
# Completed 11/30/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Create a directed weighted graph that takes all the values provided and their inverse
2. For each query, bfs to find whether path exists
"""

from collections import deque

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class Solution:
    def _create_graph(self, equations, values):
        self.graph = {}
        for div, value in zip(equations, values):
            if self.graph.get(div[0]) is None:
                self.graph[div[0]] = [(div[1], value)]
            else:
                self.graph[div[0]].append((div[1], value))
            if self.graph.get(div[1]) is None:
                self.graph[div[1]] = [(div[0], 1 / value)]
            else:
                self.graph[div[1]].append((div[0], 1 / value))

        
    def _bfs(self, start, goal, product, visited):
        if self.graph.get(start) is None or self.graph.get(goal) is None:
            return -1
        queue = deque()
        visited = [start]
        queue.append((start, 1))
        while len(queue) > 0:
            start, cur_value = queue.popleft()
            
            if start == goal:
                return cur_value
            for neighbor, value in self.graph[start]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append((neighbor, cur_value * value))
        return -1    

    def calcEquation(self, equations: [[str]], values: [float], queries: [[str]]) -> [float]:
        self._create_graph(equations, values)
        res = []
        for query in queries:
            res.append(self._bfs(str(query[0]), str(query[1]), 1, []))
        return res
            
    
        
#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    
   

if __name__ == '__main__':
    unittest.main()     