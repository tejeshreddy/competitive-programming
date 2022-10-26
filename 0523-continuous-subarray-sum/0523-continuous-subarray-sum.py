class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hmap ={0: 0}
        s = 0
        
        for i in range(len(nums)):
            s += nums[i]
            if s % k not in hmap:
                hmap[s % k] = i + 1
            elif hmap[s % k] < i:
                return True
        return False
        