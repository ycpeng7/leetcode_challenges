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
Iterative
1. temp = cur.next
2. cur.next = Prev
3. prev = cur
4. cur = temp
 
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
    def reverseList_itr(self, head: ListNode) -> ListNode:
        cur = head
        prev = None
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

                        
#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()