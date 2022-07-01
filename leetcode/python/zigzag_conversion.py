"""
Title: 0006 - ZigZag Conversion
Tags: String
Time: O(n)
Space: O(1)
Source: https://leetcode.com/problems/zigzag-conversion/
Difficulty: Medium
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        step = 2*numRows - 2
        zigzag = ""
        
        for i in range(numRows):
            for j in range(i, len(s), step):
                zigzag = zigzag + s[j]
                if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
                    zigzag += s[j + step - 2 * i]
        return zigzag
