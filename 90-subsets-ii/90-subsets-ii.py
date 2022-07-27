class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        
        def backtracking(start, end, tmp):
            result.append(tmp[:])
            
            for i in range(start, end):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                tmp.append(nums[i])
                backtracking(i + 1, end, tmp)
                tmp.pop()
        
        nums.sort()
        result = []
        backtracking(0, len(nums), [])
        return result
            
            
        