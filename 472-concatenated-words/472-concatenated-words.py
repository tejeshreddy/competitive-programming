class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        
        @lru_cache(None)
        def goodWord(given_word):
            for i in range(len(given_word)):
                prefix = given_word[:i]
                suffix = given_word[i:]
                
                if prefix in wordSet and (suffix in wordSet or goodWord(suffix)):
                    return True
        result = []
        for given_word in words:
            if goodWord(given_word):
                result.append(given_word)
                
        return result