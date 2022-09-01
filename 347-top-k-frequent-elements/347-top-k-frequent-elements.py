class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = collections.Counter(nums)
        heap = []
        for key, v in hmap.items():
            heapq.heappush(heap, [-v, key])
        
        result = []
        while k > 0:
            v, key = heapq.heappop(heap)
            result.append(key)
            k -= 1
            
        return result
            
            
        
