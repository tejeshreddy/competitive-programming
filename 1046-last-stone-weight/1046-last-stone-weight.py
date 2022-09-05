class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * i for i in stones]
        heapq.heapify(stones)
        
        
        while len(stones) > 1:
            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1
            
            if x == y:
                continue
            else:
                heapq.heappush(stones, (y - x) * -1)
        if len(stones) > 0:
            return stones[0] * -1
        return 0
        