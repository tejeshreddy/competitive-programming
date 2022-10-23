class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        counter = collections.Counter(nums)
        result = [0, 0]
        for n in range(1, len(nums) + 1):
            
            if n not in counter:
                result[1] = n
            if counter[n] == 2:
                result[0] = n
        return result
                
        