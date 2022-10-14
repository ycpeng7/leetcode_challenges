class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = "1234567890abcdefghijklmnopqrstuvwxyz"
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].lower() not in alphanumeric:
                i += 1
                continue
            if s[j].lower() not in alphanumeric:
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
