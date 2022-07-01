"""
Title: 0011 - Container With Most Water
Tags: Array
Time: O(n)
Space: O(1)
Source: https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, max_area = 0, len(height)-1, 0
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return(max_area)
            
    # Below approach: Time Limit Exceeded
    def maxArea1(self, height: List[int]) -> int:
        m_vol = -1
        for i in range(len(height)):
            for j in range(i, len(height)):
                if i != j:
                    l_vol = min(height[i], height[j]) * (j-i)
                    if  l_vol > m_vol:
                        m_vol = l_vol
        return m_vol
