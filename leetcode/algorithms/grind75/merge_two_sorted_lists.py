# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val > list2.val:
            head = list2
            tail = list1
        else:
            head = list1
            tail = list2
        head.next = self.mergeTwoLists(head.next, tail)
        return head