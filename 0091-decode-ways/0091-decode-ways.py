class Solution:
    def __init__(self):
        self.visited = ()
    
    @lru_cache(None)
    def dfs(self, s):
        if len(s) > 0:
            if s[0] == "0":
                return 0
        
        if len(s) == 1 or s == "":
            return 1
        
        if int(s[:2]) <= 26:
            first = self.dfs(s[1:])
            second = self.dfs(s[2:])
            return first + second
        else:
            return self.dfs(s[1:])
        
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        if len(s) == 1:
            return 1
        
        return self.dfs(s)
        
        
        