class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = collections.Counter(nums)
        hmap = dict(sorted(hmap.items(), key=lambda x: x[1], reverse = True))
        return list(hmap.keys())[:k]
        
        
        