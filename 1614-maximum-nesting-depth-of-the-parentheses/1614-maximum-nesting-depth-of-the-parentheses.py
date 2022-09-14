class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        result = 0
        
        for c in s:
            if c == "(":
                count += 1
                result = max(count, result)
            if c == ")":
                count -= 1
        return result
                
        