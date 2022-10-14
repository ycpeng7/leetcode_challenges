class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        If there exists a cycle, given two indexes i and j that each increment by 1 and 2, respectively, they
        must collide at some point.
        """
        
        if head is None:
            return False
        
        i = head.next
        
        if i is None:
            return False
        else:
            j = i.next
        
        while i != j:
            if i is None or j is None or j.next is None:
                return False
            else:
                i = i.next
                j = j.next.next
        
        return True