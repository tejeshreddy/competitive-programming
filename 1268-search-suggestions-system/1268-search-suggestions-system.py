class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.suggestions = []
    
    def add_suggestion(self, product):
        if len(self.suggestions) < 3:
            self.suggestions.append(product)

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        
        
        for p in products:
            node = self.root
            for char in p:
                node = node.children[char]
                node.add_suggestion(p)
        
        result, node = [], self.root
        
        for char in searchWord:
            node = node.children[char]
            result.append(node.suggestions)
        return result
        
        
        
        
        