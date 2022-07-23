class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = collections.defaultdict(int)
        
        l = 0
        maxf = 0
        
        for r in range(len(s)):
            hmap[s[r]] += 1
            
            if (r - l + 1) - max(hmap.values()) > k:
                hmap[s[l]] -= 1
                l += 1
            maxf = max(maxf, r - l + 1)
        return maxf
            
            
            
            