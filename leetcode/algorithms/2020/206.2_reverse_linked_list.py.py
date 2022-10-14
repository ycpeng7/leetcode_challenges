#-------------------------------------------------------------------------------
#    Reverse Linked List
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/reverse-linked-list/
# Completed 11/24/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Recursive
1. If cur.next or cur is None, return head as new head
2. call function
3. cur.next.next = cur
4. cur.next = None
 
Time: O(n)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

                        
#-------------------------------------------------------------------------------
#    Unit Test`
#-------------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()