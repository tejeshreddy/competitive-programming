class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        diff = []
        N = len(nums)
        
        for i in range(len(nums)):
            diff.append(nums[i] - i)
        
        hmap = collections.Counter(diff)
        
        good_pairs = 0
        
        for k, v in hmap.items():
            good_pairs += (v*(v - 1)) // 2
        
        return (N * (N - 1)) // 2 - good_pairs