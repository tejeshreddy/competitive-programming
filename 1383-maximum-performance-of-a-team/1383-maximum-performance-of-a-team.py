class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eff = [(e, s) for e, s in zip(efficiency, speed)]
        eff.sort(reverse = True)
        heap = []
        speed, result = 0, 0
        
        for e, s in eff:
            if len(heap) == k:
                speed -= heapq.heappop(heap)
            speed += s
            result = max(speed * e, result)
            heapq.heappush(heap, s)
        return result % (10 ** 9 + 7)
            
        
        