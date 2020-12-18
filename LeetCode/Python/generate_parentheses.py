"""
Title: 0022 - Generate Parentheses
Tags: String
Time: O(4^n / n^(3/2))
Space: O(n)
Source: https://leetcode.com/problems/generate-parentheses/
Difficulty: Medium
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, curr = [], []
        stk = [(1, (n, n))]
        while stk:
            step, args = stk.pop()
            if step == 1:
                left, right = args
                if left == 0 and right == 0:
                    result.append("".join(curr))
                if left < right:
                    stk.append((3, tuple()))
                    stk.append((1, (left, right-1)))
                    stk.append((2, (')')))
                if left > 0:
                    stk.append((3, tuple()))
                    stk.append((1, (left-1, right)))
                    stk.append((2, ('(')))
            elif step == 2:
                curr.append(args[0])
            elif step == 3:
                curr.pop()
        return result
