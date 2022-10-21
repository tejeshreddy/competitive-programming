class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hmap = {}
        for key, v in enumerate(nums):
            hmap[v] = hmap.get(v, []) + [key]
        
        for v in hmap.values():
            for i in range(len(v) - 1):
                if v[i + 1] - v[i] <= k:
                    print(v[i + 1], v[i])
                    return True
        return False
        
        
                
                
                
                
                
                
        
                
            
            
                    
        
        