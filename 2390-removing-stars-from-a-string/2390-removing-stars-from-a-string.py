class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "*":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(char)
        return "".join(stack)