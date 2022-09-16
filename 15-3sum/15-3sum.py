class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if i> 0 and nums[i] == nums[i - 1]:
                continue
                
            first = nums[i]
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                total = first + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    result.append([first, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result
                    
                
                
                
        