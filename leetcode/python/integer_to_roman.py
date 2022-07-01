"""
Title: 0012 - Integer to Roman
Tags: String
Time: O(n)
Space: O(1)
Source: https://leetcode.com/problems/integer-to-roman/
Difficulty: Medium
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        
        numeral_map = {
            1: "I", 4: "IV", 5: "V", 9: "IX", \
            10: "X", 40: "XL", 50: "L", 90: "XC", \
            100: "C", 400: "CD", 500: "D", 900: "CM", \
            1000: "M"
        }
        
        sorted_keys, result = sorted(numeral_map), ""
        
        while num > 0:
            for key in reversed(sorted_keys):
                while int(num / key) > 0:
                    num -= key
                    result += numeral_map[key]
                    print(key, num, numeral_map[key])
        
        return result
