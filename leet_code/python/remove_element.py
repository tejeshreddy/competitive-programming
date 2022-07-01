"""
Title: 0027 - Remove Element
Tags: Array
Time: O(n)
Space: O(1)
Source: https://leetcode.com/problems/remove-element/
Difficulty: Easy
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            i, last = 0, len(nums) - 1
            while i <= last:
                if nums[i] == val:
                    nums[i], nums[last] = nums[last], nums[i]
                    last -= 1
                else:
                    i = i+1
            return last + 1
