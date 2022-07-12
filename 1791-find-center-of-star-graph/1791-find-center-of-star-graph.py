class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hmap = {}
        for values in edges:
            for k in values:
                hmap[k] = hmap.get(k, 0) + 1
        
        hmap = dict(sorted(hmap.items(), key = lambda x: x[1], reverse=True))

        return list(hmap.keys())[0]
                
            
            
            
        