"""
Title: 0030 - Substring with Concatenation of All Words
Tags: Binary Search
Time: O(logn) = O(1)
Space: O(1)
Source: https://leetcode.com/problems/divide-two-integers/
Difficulty: Medium
"""

# Issue with finding the duplicate
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len, arr_len = len(words[0]), len(words)
        result = []
        
        for i in range(0, len(s), word_len):
            if all([w in s[i:i + word_len * arr_len] for w in words]):
                result.append(i)
        
        return result