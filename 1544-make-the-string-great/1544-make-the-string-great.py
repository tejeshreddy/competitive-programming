class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c.isupper() and c.lower() == stack[-1]:
                    stack.pop()
                    continue
                elif c.islower() and c.upper() == stack[-1]:
                    stack.pop()
                    continue
                else:
                    stack.append(c)
        return "".join(stack)
        