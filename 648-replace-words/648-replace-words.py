class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.word = None

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        cur = self.root
        
        for char in word:
            cur = cur.children[char]
        cur.word = word
    
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return word
            cur = cur.children[c]
            if cur.word != None:
                return cur.word
        return word
            

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        return " ".join(trie.search(word) for word in sentence.split())
        