class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtracking(target, temp, start, end):
            if target < 0:
                return
            
            if target == 0:
                result.append(temp[:])
            
            for i in range(start, end):
                temp.append(candidates[i])
                backtracking(target - candidates[i], temp, i, end)
                temp.pop()
                
        backtracking(target, [], 0, len(candidates))
        
        return result
        