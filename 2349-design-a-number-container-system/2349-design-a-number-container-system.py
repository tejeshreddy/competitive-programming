from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.hmap = collections.defaultdict(SortedList)
        self.idx = {}

    def change(self, index: int, number: int) -> None:
        if index in self.idx:
            old = self.idx[index]
            self.hmap[old].discard(index)
            if len(self.hmap[old]) == 0:
                del self.hmap[old]
        self.hmap[number].add(index)
        self.idx[index] = number
            

    def find(self, number: int) -> int:
        if number in self.hmap:
            return self.hmap[number][0]
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)