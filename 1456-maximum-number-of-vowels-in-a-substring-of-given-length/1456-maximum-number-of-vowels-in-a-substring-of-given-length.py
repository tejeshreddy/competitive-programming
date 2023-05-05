class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, r = 0, k - 1
        vowelc = 0
        max_vowels = 0
        vowels = ('a', 'e', 'i', 'o', 'u')
        
        for i in range(l, r + 1):
            if s[i] in vowels:
                vowelc += 1
        
        max_vowels = max(vowelc, max_vowels)
        while r + 1 < len(s):
            if s[l] in vowels:
                vowelc -= 1
            l += 1
            r += 1
            if s[r] in vowels:
                vowelc += 1
            max_vowels = max(vowelc, max_vowels)
        return max_vowels
                
            
        