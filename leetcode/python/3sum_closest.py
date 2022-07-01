"""
Title: 0016 - 3Sum Closest
Tags: Two Pointers
Time: O(n^2)
Space: O(1)
Source: https://leetcode.com/problems/3sum-closest/
Difficulty: Medium
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result, min_diff = 0, float("inf")
        nums.sort()
        
        for i in range(len(nums)-1, 1, -1):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                continue
            left, right = 0, i-1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return target
                
                if abs(total - target) < min_diff:
                    min_diff = abs(total - target)
                    result = total
        return result
