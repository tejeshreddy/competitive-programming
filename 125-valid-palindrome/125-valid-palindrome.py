class Solution:
    def isPalindrome(self, s: str) -> bool:
        resulting_string = ""
        for char in s:
            if char.isalnum():
                resulting_string += char.lower()
        
        return resulting_string == resulting_string[::-1]
    
        