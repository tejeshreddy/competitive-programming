"""
Title: 0026 - Remove Duplicates from Sorted Array
Tags: Array
Time: O(n)
Space: O(1)
Source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Difficulty: Easy
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        last = 0
        for i in range(len(nums)):
            if nums[i] != nums[last]:
                last += 1
                nums[last] = nums[i]
        return last + 1
