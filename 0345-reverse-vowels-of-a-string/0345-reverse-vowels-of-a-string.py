class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        values = []
        string = ""
        for c in s:
            if c not in vowels:
                string += c
            else:
                string += "*"
                values.append(c)
        
        s = ""
        values.reverse()
        
        for c in string:
            if c != "*":
                s += c
            else:
                x = values.pop(0)
                s += x
        return s
            
                
        