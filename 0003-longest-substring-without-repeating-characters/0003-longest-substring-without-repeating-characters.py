class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        visited = set()
        result = 0
        
        while r < len(s):
            if s[r] not in visited:
                visited.add(s[r])
                r += 1
            else:
                while s[r] in visited:
                    visited.remove(s[l])
                    l += 1
            result = max(result, len(visited))
        return result
                    
            
        