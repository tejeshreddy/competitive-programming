class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = k
        hmap = collections.Counter(nums)
        
        heap = []
        for k, v in hmap.items():
            heapq.heappush(heap, [-v, k])
        
        result = []
        for i in range(1, count + 1):
            v, k = heapq.heappop(heap)
            result.append(k)
        
        return result
            
        
        