class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def dfs(temp, i):
            if i == len(nums):
                result.append(temp[:])
                return
            temp.append(nums[i])
            dfs(temp, i + 1)
            temp.pop()
            dfs(temp, i + 1)
        
        dfs([], 0)
        return result
                
        
        
        
        
        