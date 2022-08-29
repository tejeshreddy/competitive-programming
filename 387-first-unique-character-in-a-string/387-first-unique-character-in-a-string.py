class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = {}
        
        for c in s:
            hmap[c] = hmap.get(c, 0) + 1
            
        for k, c in enumerate(s):
            if hmap[c] == 1:
                return k
        return -1
        