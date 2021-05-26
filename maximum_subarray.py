"""
Title: 0053 - Maximum Subarray
Tags: Dynamic Programming
Time: O(n)
Space: O(1)
Source: https://leetcode.com/problems/maximum-subarray/
Difficulty: Easy
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        gsum, lsum = float("-inf"), 0
        
        if len(nums) == 1:
            return nums[0]
        
        for i in nums:
            lsum += i
            if lsum > gsum:
                gsum = lsum
            if lsum < 0:
                lsum = 0
        return gsum
        