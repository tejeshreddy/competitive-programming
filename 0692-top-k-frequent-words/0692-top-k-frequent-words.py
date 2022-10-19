class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        word_map = collections.Counter(words)
        word_map = dict(sorted(word_map.items(), key = lambda x: (-x[1], x[0])))
        return list(word_map.keys())[:k]
        
        
        