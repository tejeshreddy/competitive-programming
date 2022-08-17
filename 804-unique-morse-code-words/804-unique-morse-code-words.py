class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        visit = set()
        
        for w in words:
            s = ""
            for c in w:
                s += morse[ord(c) - ord("a")]
            visit.add(s)
        return len(visit)
                
        