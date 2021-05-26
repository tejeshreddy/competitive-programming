"""
Title: 0058 - Length of Last Word
Tags: String
Time: O(n)
Space: O(1)
Source: https://leetcode.com/problems/length-of-last-word/
Difficulty: Easy
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.strip() == "":
            return 0
        
        return len(s.split()[-1])
