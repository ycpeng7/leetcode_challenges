class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Two pointers
        
        1. i , j start from 0
        2. j keeps increasing, store index of letter in hashmap, until there's duplicate
        3. Calculate length of i ~ j-1 and compare with current length
        4. i moves to s[j] + 1 ONLY IF THIS INDEX IS LARGER THAN I,
        because if it is smaller, we might jump to a point where there are duplicates ahead.
        5. j continues, if j hits the end, also calculate the length
        
        """
        
        hashmap = {}
        
        n = len(s)
        
        if n <= 1:
            return n
        
        i = j = 0
        longest = 1
        
        while j < n:
            if hashmap.get(s[j]) is None:
                hashmap[s[j]] = j
            else:
                longest = max(longest, j - i)
                i = max(i, hashmap[s[j]] + 1)
                hashmap[s[j]] = j
            j += 1
        
        return max(longest, j - i)