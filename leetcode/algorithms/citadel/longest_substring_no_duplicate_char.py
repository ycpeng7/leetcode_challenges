

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Two pointers
        
        1. i start from 0, j from 1
        2. j keeps increasing, store index of letter in hashmap, until there's duplicate
        3. Calculate length of i ~ j-1 and compare with current length
        4. i moves to the duplicate position (stored in hashmap) + 1 ONLY IF THIS INDEX IS LARGER THAN I,
        because if it is smaller, we might jump to a point where there are duplicates ahead.
        5. j continues, if j hits the end, also calculate the length
        
        """
        input = s
        
        hashmap = {}

        length = len(input)

        if length <= 1:
            return length
    
        max_length = 0

        i = 0
        j = 0

        while(j < length):
            print(max_length)
            if hashmap.get(s[j]) is None:
                hashmap[s[j]] = j

            else:
                max_length = max(max_length, j - i)
                i = max(i, hashmap[s[j]] + 1)
                hashmap[s[j]] = j

            j += 1
        
        max_length = max(max_length, j - i)
                
        return max_length