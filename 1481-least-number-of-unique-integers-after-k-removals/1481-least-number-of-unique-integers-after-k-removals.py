class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hmap = {}
        for i in arr:
            hmap[i] = hmap.get(i, 0) + 1
            
        hmap = dict(sorted(hmap.items(), key = lambda x: x[1]))
        zero_count = 0
        
        for key, value in hmap.items():
            if value <= k:
                k -= hmap[key]
                zero_count += 1
        print(hmap, zero_count)
        return len(hmap) - zero_count
            
                