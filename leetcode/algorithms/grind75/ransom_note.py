class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        1. Construct a hashmap of letter to count from magazine
        2. For each letter in ransomNote, deduct one from hashmap, if non-existant or 0, return false
        3. Return true
        """
        
        hashmap = {}
        
        for char in magazine:
            if hashmap.get(char) is None:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
                
        for char in ransomNote:
            if hashmap.get(char) is None or hashmap.get(char) == 0:
                return False
            else:
                hashmap[char] -= 1
        
        return True
        