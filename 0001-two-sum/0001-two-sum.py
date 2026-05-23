class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i, n in enumerate(nums):
            if n in hmap:
                return [hmap[n], i]
            hmap[target - n] = i
