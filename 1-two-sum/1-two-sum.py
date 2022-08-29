class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = collections.defaultdict(int)
        
        for k, i in enumerate(nums):
            if target - i in hmap:
                return [k, hmap[target - i]]
            else:
                hmap[i] = k
        