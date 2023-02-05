class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        
        p_hmap = collections.Counter(p)
        s_hmap = collections.Counter(s[:len(p)])
        l, r = 0, len(p)
        
        while r <= len(s):
            
            if p_hmap == s_hmap:
                result.append(l)
            
            s_hmap[s[l]] = s_hmap[s[l]] - 1
            if s_hmap[s[l]] <= 0:
                s_hmap.pop(s[l])
            
            if r < len(s):
                s_hmap[s[r]] += 1
                
            l += 1
            r += 1
            
        return result
