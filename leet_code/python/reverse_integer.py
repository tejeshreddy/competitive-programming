"""
Title: 0007 - Reverse Integer
Tags: Math
Time: O(logn)
Space: O(1)
Source: https://leetcode.com/problems/reverse-integer/
Difficulty: Easy
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -self.reverse(-x)
        
        result = 0
        while x:
            result = result * 10 + x % 10
            x //= 10
        return result if result <= 0x7fffffff else 0
