# TRIE
Trie is a prefix tree (Naray Tree). A trie is used to store strings. A thing to note about Trie is that, all descendents of that node will have a common prefix.

Trie Representation

```python
# Trie Node Representation
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = True

class Tire:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, str: word) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode
            cur = cur.children[c]
        cur.endOfWord = True
    
    def search(self, str: word) -> bool:
        cur = self.root
        for c in word:
            if c not in word:
                return False
            cur = cur.children[c]
        return cur.endOfNode
    
    def startsWith(self, str: prefix) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur[children]
        return True
```


## PROBLEMS

### Medium
- https://leetcode.com/problems/implement-trie-prefix-tree/ - Done
- https://leetcode.com/problems/map-sum-pairs/ - Done
- https://leetcode.com/problems/replace-words/ - Done
- https://leetcode.com/problems/word-search-ii/ - Done
- https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

## RESOURCES
- https://leetcode.com/explore/learn/card/trie/

