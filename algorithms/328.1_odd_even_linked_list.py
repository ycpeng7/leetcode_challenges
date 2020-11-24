#-------------------------------------------------------------------------------
#    Odd Even Linked List
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/odd-even-linked-list/
# Completed 11/24/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Keep track of odd and even head
2. temp = cur.next
3. cur.next = cur.next.next
4. prev = cur
5. cur = temp
6. If cur.next is None, check whether it's odd or even
7. If odd, cur.next = even head, else prev.next = even head

Time: O(n)
Space: O(1)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        even_head = head.next
        cur = head
        count = 1
        while cur.next is not None:
            temp = cur.next
            cur.next = cur.next.next
            prev = cur
            cur = temp
            count += 1
        if count % 2 == 1:
            cur.next = even_head
        else:
            prev.next = even_head
        return head


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest


if __name__ == '__main__':
    unittest.main()