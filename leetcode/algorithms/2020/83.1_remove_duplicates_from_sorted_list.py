#-------------------------------------------------------------------------------
#    Remove Duplicates from Sorted List
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Completed 11/24/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Make cur.next as temp
2. Keep moving temp forward until value is not duplicated
3. cur.next = temp
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur is not None and cur.next is not None:
            value = cur.val
            temp = cur.next
            while temp is not None and temp.val == value:
                temp = temp.next
            cur.next = temp
            cur = temp
        return head                   


#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest


if __name__ == '__main__':
    unittest.main()