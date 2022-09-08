class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        dp.append(True) 
        for i in range(len(s), -1, -1):
            for word in wordDict:
                if word == s[i: i + len(word)]:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]
        