"""
Title: 0020 - Valid Parentheses
Tags: String
Time: O(n)
Space: O(n)
Source: https://leetcode.com/problems/integer-to-roman/
Difficulty: Medium
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for i in s:
            if i in pairs:
                if len(stack) != 0:
                    if stack[-1] == pairs[i]:
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return True if len(stack) == 0 else False
