class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0" or s is None:
            return 0
        
        @lru_cache()
        def dfs(string):
            if len(string) > 0:
                if string[0] == "0":
                    return 0
            if len(string) == 1 or string == "":
                return 1
                
            if int(string[0:2]) <= 26:
                res1 = dfs(string[1:])
                res2 = dfs(string[2:])
                return res1 + res2
            else:
                return dfs(string[1:])
        return dfs(s)
        