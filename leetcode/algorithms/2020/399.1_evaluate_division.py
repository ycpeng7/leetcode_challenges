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
2. For each query, dfs to find whether path exists
"""


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

        
    def _dfs(self, start, goal, product, visited):
        if self.graph.get(start) is None or self.graph.get(goal) is None or start in visited:
            return -1
        visited.append(start)
        for neighbor, value in self.graph[start]:
            print(neighbor, value)
            if neighbor == goal:
                return product * value
            else:
                product_updated = self._dfs(neighbor, goal, product * value, visited)
                if product_updated != -1:
                    return product_updated
        return -1


    def calcEquation(self, equations: [[str]], values: [float], queries: [[str]]) -> [float]:
        self._create_graph(equations, values)
        res = []
        for query in queries:
            res.append(self._dfs(str(query[0]), str(query[1]), 1, []))
        return res
            
    
        
#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    
   

if __name__ == '__main__':
    unittest.main()     