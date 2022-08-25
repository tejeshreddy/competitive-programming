class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        self.result = ""
        
        def palindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(self.result):
                    self.result = s[l:r+1]
                
                l -= 1
                r += 1

            return
        
        for i in range(len(s)):
            print(i)
            palindrome(i, i)
            palindrome(i, i + 1)
        return self.result
        