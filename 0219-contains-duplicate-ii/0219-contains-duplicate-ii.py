class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}
        
        for key, value in enumerate(nums):
            if value in hmap and key - hmap[value] <= k:
                return True
            hmap[value] = key
        return False