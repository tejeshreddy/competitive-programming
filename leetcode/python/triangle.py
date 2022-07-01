"""
Title: 0120 - Triangle
Tags: Dynamic Programming
Time: O(n^2)
Space: O(n^2)
Source: https://leetcode.com/problems/triangle/
Difficulty: Medium
"""

import collections

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        result = collections.defaultdict(list)
        result[len(triangle) - 1] = triangle[len(triangle) - 1]
        
        print(result)
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                result[i].append(min(triangle[i][j] + result[i + 1][j], triangle[i][j] + result[i + 1][j + 1]))
        return result[0][0]
   
