class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hmap = collections.Counter(nums)
        for k, v in hmap.items():
            if v != 3:
                return k