class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = "1234567890abcdefghijklmnopqrstuvwxyz"
        i = 0
        j = len(s)-1
        while i < j:
            left = s[i].lower()
            right = s[j].lower()
            if left not in alphanumeric:
                i+=1
                continue
            elif right not in alphanumeric:
                j-=1
                continue
            elif left != right:
                return False
            else:
                i+=1
                j-=1
        return True
            