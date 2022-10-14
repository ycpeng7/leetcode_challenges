#-------------------------------------------------------------------------------
#    Implement Stack using Queues
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/implement-stack-using-queues/
# Completed 11/23/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Implement stack with two queues (deque)
2. When pop is executed, keep popping q1 and append to q2 until len(q1) == 1
3. Return the last element of q1, then set q1 = q2 

Time: O(n) for push and pop
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.appendleft(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        q2 = deque()
        while len(self.q1) > 1:
            q2.appendleft(self.q1.pop())
        top = self.top()
        self.q1 = q2
        return top

        """
        only 1 queue:
        n = len(self.q1)
        while n > 1:
            self.q1.appendleft(self.q1.pop())
            n -= 1
        return self.q1.pop()
        """

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0