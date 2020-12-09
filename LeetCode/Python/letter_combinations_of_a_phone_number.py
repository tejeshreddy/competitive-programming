"""
Title: 0017 - Letter Combinations of a Phone Number
Tags: String
Time: O(n * 4^n)
Space: O(1)
Source: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Difficulty: Medium
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = [""]
        lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        for digit in reversed(digits):
            choices = lookup[int(digit)]
            m, n = len(choices), len(result)
            result.extend([result[i % n] for i in range(n, m*n)])
            for i in range(m*n):
                result[i] = choices[i//n] + result[i]
        
        return result
