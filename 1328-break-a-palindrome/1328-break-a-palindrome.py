class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        def check(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        smallest = "z" * len(palindrome)
        
        for i in range(len(palindrome)):
            for j in range(0, 27):
                temp = palindrome[:i] + chr(ord("a") + j) + palindrome[i + 1: ]
                if temp < smallest and not check(temp) :
                    smallest = temp
        return smallest
        
        
        
            
        