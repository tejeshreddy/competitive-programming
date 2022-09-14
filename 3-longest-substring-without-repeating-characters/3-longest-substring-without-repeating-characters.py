class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = set()
        l= 0
        max_ = 0
        
        for r in range(len(s)):
            
            while s[r] in cur:
                cur.remove(s[l])
                l += 1
            max_ = max(max_, r - l + 1)
            cur.add(s[r])
        return max_
