class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(path, candidates, start, target):
            if target == 0:
                result.append(path)
                return
            if target < 0 or start >= len(candidates):
                return
            
            for i in range(start, len(candidates)):
                dfs(path + [candidates[i]], candidates, i, target - candidates[i])
        
        dfs([], candidates, 0, target)
        return result
                
        
        