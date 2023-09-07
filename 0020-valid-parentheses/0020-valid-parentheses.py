class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in hmap:
                if len(stack) == 0:
                    return False
                elif stack[-1] == hmap[char]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return len(stack) == 0
        
        