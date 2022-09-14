class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.result = ""
        length = len(s)
        
        def check_palindrome(l, r):
            while l >= 0 and r < length and s[l] == s[r]:
                if (r - l + 1) > len(self.result):
                    self.result = s[l:r + 1]
                l -= 1
                r += 1
            return
            
                
        
        for i in range(length):
            check_palindrome(i, i)
            check_palindrome(i, i + 1)
        
        return self.result
                
                    
            
        