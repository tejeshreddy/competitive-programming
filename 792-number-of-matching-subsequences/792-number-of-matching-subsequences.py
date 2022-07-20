class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        count = 0
        subsequence = set()
        notsubsequence = set()
        for word in words:
            if word in subsequence:
                count += 1
                continue
            if word in notsubsequence:
                continue
            
            i, j = 0, 0
            
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            
            if j == len(word):
                count += 1
                subsequence.add(word)
            else:
                notsubsequence.add(word)
        
        return count