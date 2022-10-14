#-------------------------------------------------------------------------------
#    Add Two Numbers
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/add-two-numbers/
# Completed 12/3/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Start from head
2. While l1 or l2 is not null, keep advancing
3. Add l1 and l2 as value of l3, keep carry in mind


Time: O(n)
Space: O(n)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        l3_head = l3
        carry = 0
        while l1 is not None or l2 is not None:
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val
            _sum = l1_val + l2_val + carry
            carry = 0
            if _sum >= 10:
                carry = _sum // 10
                _sum = _sum % 10
            l3.val = _sum
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            l3.next = ListNode()
            prev = l3
            l3 = l3.next
        if carry > 0:
            l3.val = carry
        else:
            del l3
            prev.next = None
        return l3_head


        


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest


if __name__ == '__main__':
    unittest.main()