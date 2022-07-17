class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        N = len(nums[0])
        hmap = collections.defaultdict(list)
        result = []
        
        for k, trim in queries:
            if trim not in hmap:
                trimmed_values = [int(n[N - trim: ]) for n in nums]
                hmap[trim] = trimmed_values
            else:
                trimmed_values = hmap[trim]
            positions = [(v, k) for k, v in enumerate(trimmed_values)]
            positions = sorted(positions, key=lambda x: x[0])

            result.append(positions[k - 1][1])
        return result
            
            
                
                    
        