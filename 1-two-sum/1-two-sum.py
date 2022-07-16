class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        k = target
        for n in range(len(nums)):
            if k - nums[n] in hmap:
                return [hmap[k - nums[n]], n]
            else:
                hmap[nums[n]] = n
        
                
        