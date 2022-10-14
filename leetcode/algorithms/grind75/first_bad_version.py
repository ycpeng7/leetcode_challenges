# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Binary search
        1. Binary search takes two index
        2. if mid_ind is good, search mid_ind + 1, end
        3. if the mid index is bad and previous isn't, return it
        4. Otherwise, search start, mid_ind - 1 
        
        """
        if n == 1:
            return 1
        
        def binary_search(start, end) -> int:
            new_n = (start + end) // 2
            
            if not isBadVersion(new_n):
                return binary_search(new_n + 1, end)
            else:
                if new_n == 1 or not isBadVersion(new_n - 1):
                    return new_n
                else:
                    return binary_search(start, new_n - 1)
    
        return binary_search(1, n)