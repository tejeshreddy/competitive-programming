"""
Title: 0008 - String to Integer (atoi)
Tags: String
Time: O(n)
Space: O(1)
Source: https://leetcode.com/problems/string-to-integer-atoi/
Difficulty: Medium
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX =  2147483647
        INT_MIN = -2147483648
        result = 0

        if not s:
            return result

        i = 0
        while i < len(s) and s[i].isspace():
            i += 1

        if len(s) == i:
            return result

        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        while i < len(s) and '0' <= s[i] <= '9':
            if result > (INT_MAX - int(s[i])) / 10:
                return INT_MAX if sign > 0 else INT_MIN
            result = result * 10 + int(s[i])
            i += 1

        return sign * result
