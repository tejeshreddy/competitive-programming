"""
Title: 0027 - Remove Element
Tags: Array
Time: O(n + k)
Space: O(k)
Source: https://leetcode.com/problems/implement-strstr/
Difficulty: Easy
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1
