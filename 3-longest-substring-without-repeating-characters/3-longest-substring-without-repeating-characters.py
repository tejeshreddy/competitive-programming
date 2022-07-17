class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        current = set()
        l, r = 0, 0
        max_len = 0
        
        while r < len(s):
            print(current)
            while s[r] in current:
                current.remove(s[l])
                l += 1
            max_len = max(max_len, r - l + 1)
            current.add(s[r])
            r += 1
            
        return max_len