"""
Title: 0035 - Search Insert Position
Tags: Binary Search
Time: O(logn)
Space: O(1)
Source: https://leetcode.com/problems/search-insert-position/
Difficulty: Easy
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) / 2
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid -1
            else:
                low = mid + 1
            print(low, mid, high)
        return low
