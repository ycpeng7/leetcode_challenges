#-------------------------------------------------------------------------------
#    Reconstruct Itinerary
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/reconstruct-itinerary/
# Completed 12/1/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Form up a directed graph
2. Use backtracking with the ending condition of len(route) == len(tickets) + 1
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
from collections import OrderedDict

class Solution:
    def _backtracking(self, start, route):
        if len(route) == self.target_length:
            self.itinerary = route
            return True
        else:
            for neighbor, visited in self.graph[start].items():
                if not visited:
                    self.graph[start][neighbor] = True
                    res = self._backtracking(neighbor, route + [neighbor])
                    self.graph[start][neighbor] = False
                    if res:
                        return True
            return False

    def findItinerary(self, tickets: [[str]]) -> [str]:
        self.graph = {}
        self.target_length = len(tickets) + 1
        for ticket in tickets:
            if self.graph.get(ticket[0]) is None:
                self.graph[ticket[0]] = {ticket[1]: False}
            else:
                self.graph[ticket[0]][ticket[1]] = False
                self.graph[ticket[0]] = OrderedDict(sorted(self.graph[ticket[0]].items()))
        self.itinerary = []
        self._backtracking('JFK', ['JFK'])
        return self.itinerary

    
        
#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_generic(self):
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        res = ["JFK", "MUC", "LHR", "SFO", "SJC"]
        self.assertEqual(Solution().findItinerary(tickets), res)
    def test_lexical_order(self):
        tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        res = ["JFK","ATL","JFK","SFO","ATL","SFO"]
        self.assertEqual(Solution().findItinerary(tickets), res)

    
   

if __name__ == '__main__':
    unittest.main()     