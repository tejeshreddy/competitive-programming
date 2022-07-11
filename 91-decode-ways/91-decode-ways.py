class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s is None:
            return 0

        @lru_cache(maxsize=None)
        def dfs(string):
            if len(string) > 0:
                if string[0] == "0":
                    return 0
            if len(string) == 1 or string == "":
                return 1
            
            if int(string[:2]) <= 26:
                first = dfs(string[1:])
                second = dfs(string[2:]) 
                return first + second
            else:
                return dfs(string[1:])

        return dfs(s)
            