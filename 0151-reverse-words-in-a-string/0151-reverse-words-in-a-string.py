class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s = [c for c in s if c != ""]
        return " ".join(reversed(s))
        
        