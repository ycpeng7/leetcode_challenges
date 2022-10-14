class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parent_map = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if len(stack) == 0 or stack.pop() != parent_map.get(char):
                    return False
        return len(stack) == 0

assert Solution().isValid("()") == True
