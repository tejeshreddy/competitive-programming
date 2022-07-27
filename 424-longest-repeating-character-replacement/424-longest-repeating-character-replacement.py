class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        l, r = 0, 0
        hmap = collections.defaultdict(int)
        
        for r in range(len(s)):
            hmap[s[r]] += 1
            if (r - l + 1 - max(hmap.values())) <= k:
                maxf = max(maxf, r - l + 1)
            else:
                hmap[s[l]] -= 1
                l += 1
        return maxf
            
        