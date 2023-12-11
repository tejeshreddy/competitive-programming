class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
                
        for i in range(len(s) - 1):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
            
        return result
                
        
        