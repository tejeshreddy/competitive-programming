class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# LRU ---- Nodes ----- MRU        
        
class LRUCache:
    
    def __init__(self, capacity: int):
        self.hmap = {}
        self.left = Node()
        self.right = Node()
        self.left.next, self.right.prev = self.right, self.left
        self.capacity = capacity
        
    def remove(self, node):
        l, r = node.prev, node.next
        l.next, r.prev = r, l
        
    def insert(self, node):
        l, r = self.right.prev, self.right
        l.next, r.prev = node, node
        node.next, node.prev = r, l

    def get(self, key: int) -> int:
        if key in self.hmap:
            self.remove(self.hmap[key])
            self.insert(self.hmap[key])
            return self.hmap[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.remove(self.hmap[key])
        self.hmap[key] = Node(key, value)
        self.insert(self.hmap[key])
        
        if len(self.hmap) > self.capacity:
            temp = self.left.next
            self.remove(temp)
            del self.hmap[temp.key]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)