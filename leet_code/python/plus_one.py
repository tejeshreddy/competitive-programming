"""
Title: 0066 - Plus One
Tags: String
Time: O(n)
Space: O(1)
Source: https://leetcode.com/problems/plus-one/
Difficulty: Easy
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [str(i) for i in digits]
        digits = int("".join(digits)) + 1
        digits = [int(i) for i in str(digits)]
        return digits
