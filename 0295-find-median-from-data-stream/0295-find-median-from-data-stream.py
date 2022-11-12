class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)
        
        if self.small and self.large and self.small[0] * -1 > self.large[0]:
            value = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, value)
        
        if len(self.small) > len(self.large) + 1:
            value = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, value)
            
        elif len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large) * -1
            heapq.heappush(self.small, value)
            
    def findMedian(self) -> float:
        
        if len(self.small) == len(self.large):
            return (self.small[0] * -1 + self.large[0])/2
        elif len(self.small) > len(self.large):
            return self.small[0] * -1
        else:
            return self.large[0]
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()