class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True

        
        for i in range(1, len(s)+1):
            for w in wordDict:
                if i - len(w) >= 0 and dp[i - len(w)] and s[i - len(w):i] == w:
                    dp[i] = True
                
        return dp[-1]
                    
                    
        