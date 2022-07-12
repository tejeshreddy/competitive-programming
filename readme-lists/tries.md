# Trie
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


## Problems

### Medium
- https://leetcode.com/problems/implement-trie-prefix-tree/ - Done
- https://leetcode.com/problems/map-sum-pairs/ - Done
- https://leetcode.com/problems/replace-words/ - Done
- https://leetcode.com/problems/word-search-ii/ - Done
- https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

## Important Solutions
https://leetcode.com/problems/word-search-ii/

```python
class Node:
    def __init__(self):
        self.children = {}
        
        self.word = None

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        cur = trie.root
        result = set()

        def dfs(r, c, cur, visit):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] not in cur.children or (r, c) in visit:
                return
            visit.add((r, c))
            if cur.children[board[r][c]].word != None:
                result.add(cur.children[board[r][c]].word)
            dfs(r + 1, c, cur.children[board[r][c]], visit)
            dfs(r, c + 1, cur.children[board[r][c]], visit)
            dfs(r - 1, c, cur.children[board[r][c]], visit)
            dfs(r, c - 1, cur.children[board[r][c]], visit)
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in cur.children:
                    print(board[r][c])
                    dfs(r, c, cur, set())
        return list(result)
```

## Resources
- https://leetcode.com/explore/learn/card/trie/

