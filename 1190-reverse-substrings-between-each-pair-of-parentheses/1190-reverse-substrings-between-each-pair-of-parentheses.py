class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        
        stack = []
        
        for char in s:
            if char != ")":
                stack.append(char)
            else:
                to_reverse = ""
                while stack[-1] != "(":
                    to_reverse = stack.pop() + to_reverse
                stack.pop()
                to_reverse = to_reverse[::-1]
                stack.append(to_reverse)
        
        return "".join(stack)
                    