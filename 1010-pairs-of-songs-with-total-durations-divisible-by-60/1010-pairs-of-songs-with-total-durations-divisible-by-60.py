class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hmap = collections.Counter(t % 60 for t in time)
        
        
        result = (hmap.get(0, 0) * (hmap.get(0, 0) - 1)) // 2  + (hmap.get(30, 0) * (hmap.get(30, 0) - 1)) // 2
        
        # result = temp * (temp - 1) // 2
        
        visited = set([30, 0])
        for time, count in hmap.items():
            if time not in visited:
                result += hmap.get(time, 0) * hmap.get(60 - time, 0)
                visited.add(time)
                visited.add(60 - time)
        return result
                
        
        
        
        
        
        