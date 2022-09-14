class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = nums[:k]
        heapq.heapify(pq)
        
        for x in nums[k:]:
            heapq.heappush(pq, x)
            heapq.heappop(pq)
        return pq[0]
    