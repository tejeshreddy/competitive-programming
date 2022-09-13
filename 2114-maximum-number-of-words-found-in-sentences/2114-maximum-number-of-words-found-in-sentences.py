class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0
        
        for s in sentences:
            result = max(result, len(s.split(" ")))
        return result
            