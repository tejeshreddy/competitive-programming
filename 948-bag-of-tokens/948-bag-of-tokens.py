class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens = collections.deque(sorted(tokens))
        
        score = 0
        ans = 0
        
        while tokens and (power > tokens[0] or score):
            while tokens and power >= tokens[0]:
                power -= tokens.popleft()
                score += 1
            ans = max(ans, score)
            
            if tokens and score:
                power += tokens.pop()
                score -= 1
        return ans
                
            
            
                
            
        
        