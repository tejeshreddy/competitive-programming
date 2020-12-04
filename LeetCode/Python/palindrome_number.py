"""
Title: 0009 - Palindrome Number
Tags: Math
Time: O(1)
Space: O(1)
Source: https://leetcode.com/problems/palindrome-number/
Difficulty: Easy
"""

class Solution:
    # Solution 1
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        copy, reverse = x, 0 
        while copy:
            reverse = reverse * 10 + copy % 10
            copy //= 10
            
        if reverse == x:
            return True
        else:
            return False
            
    # Solution 2
    def isPalindrome1(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
