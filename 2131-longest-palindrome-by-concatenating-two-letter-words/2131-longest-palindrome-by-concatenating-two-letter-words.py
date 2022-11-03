class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        result = 0
        central = False
        
        for word, count in counter.items():
            if word[0] == word[1]:
                if count % 2 == 0:
                    result += count
                else:
                    result += count - 1
                    central = True    
            elif word[0] < word[1]:
                result += 2 * min(count, counter[word[1] + word[0]])
        
        if central:
            result += 1
        
        return (2 * result)
    
                
            
                
                
            
            
            

        