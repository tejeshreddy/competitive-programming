class Solution:
    def __init__(self):
        self.result = []
    
    def dfs(self, candidates, start, target, current_solution):
        if target == 0:
            self.result.append(current_solution)
            return
        if target < 0:
            return
        for current in range(start, len(candidates)):
            self.dfs(candidates, current, target - candidates[current], current_solution + [candidates[current]])
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        for start in range(len(candidates)):
            self.dfs(candidates, start, target - candidates[start], [candidates[start]])
        return self.result
        
        
        
        