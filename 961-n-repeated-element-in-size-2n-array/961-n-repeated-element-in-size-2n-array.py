class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums) // 2
        hmap = collections.Counter(nums)
        
        for k, v in hmap.items():
            if v == n:
                return k
        
        
        