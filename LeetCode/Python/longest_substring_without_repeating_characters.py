"""
Title: 0003 - Longest Substring Without Repeating Characters
Tags: Hash Table
Time: O(n)
Space: O(1)
Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, left = 0, 0
        look_up = {}
        for right in range(len(s)):
            if s[right] in look_up:
                left = max(left, look_up[s[right]]+1)
            look_up[s[right]] = right
            result = max(result, right-left+1)
        return result
