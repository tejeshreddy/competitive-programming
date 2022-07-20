class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        @lru_cache(None)
        def dfs(i, c):
            if i == n:
                return 1
            
            ans = 0
            if c == "a":
                ans += dfs(i + 1, "e")
            elif c =="e":
                ans += dfs(i + 1, "a") + dfs(i + 1, "i") 
            elif c == "i":
                ans += dfs(i + 1, "a") + dfs(i + 1, "e") + dfs(i + 1, "o") + dfs(i + 1, "u")
            elif c == "o":
                ans += dfs(i + 1, "i") + dfs(i + 1, "u")
            elif c == "u":
                ans += dfs(i + 1, "a")
            return ans % mod
        
        mod = 10 ** 9 + 7
        return (dfs(1, "a") + dfs(1, "e") + dfs(1, "i") + dfs(1, "o") + dfs(1, "u")) % mod
        