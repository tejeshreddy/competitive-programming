class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hmap = collections.Counter(nums)
        hmap = sorted(hmap.items(), key = lambda x: (x[1], -x[0]))
        result = []
        for k, count in hmap:
            result += [k] * count
        return result
            
        