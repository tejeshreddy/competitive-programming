class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hmap = collections.defaultdict(list)
        
        for n in nums:
            total = sum([int(i) for i in str(n)])
            
            hmap[total] = hmap[total] +[n]
            hmap[total] = sorted(hmap[total], reverse=True)[:2]
        
        result = -1
        for k, v in hmap.items():
            if len(v) == 2:
                result = max(result, sum(v))
        return result