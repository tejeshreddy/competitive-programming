class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        hmap = collections.Counter(x%k for x in arr)
        
        if 0 in hmap:
            if hmap[0] % 2 != 0:
                return False
        
        for x in hmap:
            if x > 0:
                if hmap[x] != hmap[k - x]:
                    return False
        return True
            
                
        