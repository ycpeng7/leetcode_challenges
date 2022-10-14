class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_count = {}
        
        for char in s:
            if word_count.get(char) is None:
                word_count[char] = 1
            else:
                word_count[char] += 1
        
        for char in t:
            count = word_count.get(char)
            if count is None:
                return False
            else:
                word_count[char] = count - 1
                if word_count[char] == 0:
                    word_count.pop(char)
        return len(word_count) == 0
        
        ### Method 2
        
        #lis_s = sorted(list(s))
        #lis_t = sorted(list(t))
        #return lis_s == lis_t