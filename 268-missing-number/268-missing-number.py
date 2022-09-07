class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_number = max(nums) + 2
        nums = set(nums)
        
        for i in range(max_number):
            if i not in nums:
                return i
        
        
        # for i in range(0, max(nums) + 2):
        #     if i not in nums:
        #         return i
        
        