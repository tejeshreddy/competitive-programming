class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {"a", "e", "i", "o", "u"}
        return len([i for i in s[:len(s)//2] if i.lower() in vowels]) == len([i for i in s[len(s)//2:] if i.lower() in vowels])
        