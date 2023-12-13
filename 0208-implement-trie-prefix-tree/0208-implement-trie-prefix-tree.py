class TrieNode:
    def __init__(self):
        self.children = {}
        self.eos = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            
            current = current.children[char]
        current.eos = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return current.eos
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        
        for char in prefix:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)