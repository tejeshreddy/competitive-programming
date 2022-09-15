class StockPrice:

    def __init__(self):
        self.hmap = {}
        self.min_heap = []
        self.max_heap = []
        self.latest = 0

    def update(self, timestamp: int, price: int) -> None:
        self.hmap[timestamp] = price
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))
        self.latest = max(self.latest, timestamp)
        

    def current(self) -> int:
        return self.hmap[self.latest]
        
    def maximum(self) -> int:
        while self.hmap[self.max_heap[0][1]] != -1 * self.max_heap[0][0]:
            heapq.heappop(self.max_heap)
        return -1 * self.max_heap[0][0]
        

    def minimum(self) -> int:
        while self.hmap[self.min_heap[0][1]] != self.min_heap[0][0]:
            heapq.heappop(self.min_heap)
        return self.min_heap[0][0]

        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()