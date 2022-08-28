class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        
        
        for i in range(len(nums)):
            l, r = nums[i], nums[i]
            for j in range(i, n):
                l = min(l, nums[j])
                r = max(r, nums[j])
                res += r - l
        return res
        