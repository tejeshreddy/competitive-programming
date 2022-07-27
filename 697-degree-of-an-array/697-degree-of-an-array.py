class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        positions = {}
        result = float("+inf")
        
        for i in range(len(nums)):
            if nums[i] not in positions:
                positions[nums[i]] = [i, i]
            else:
                positions[nums[i]][1] = i
        
        max_counter = max(list(counter.values()))
        
        for k, v in counter.items():
            if v == max_counter:
                pos = positions[k]
                
                result = min(result, pos[1] - pos[0] + 1)
        return result
        