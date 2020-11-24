#-------------------------------------------------------------------------------
#    Min Stack
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/min-stack/
# Completed 11/23/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Implement stack with list of [element, min_element]
2. Whenever an element is going to be pushed, check the min_element of top
3. push [element, min(element, min_element of top)]

Time: O(1) for all operations
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) > 0:
            min_element = min(x, self.getMin())
        else:
            min_element = x
        self.stack.append([x, min_element])
        

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
    