"""
Title: 0001 - Two Sum
Tags: Hash Table
Time: O(n)
Space: O(n)
Source: https://leetcode.com/problems/two-sum/
Difficulty: Easy
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff not in hmap:
                hmap[v] = i
            else:
                return [hmap[diff], i]
