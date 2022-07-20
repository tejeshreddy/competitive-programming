class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtracking(temp, target, start, end):
            if target < 0:
                return
            if target == 0:
                result.append(temp[:])
            for i in range(start, end):
                temp.append(candidates[i])
                backtracking(temp, target - candidates[i], i, end)
                temp.pop()
        
        result = []
        backtracking([], target, 0, len(candidates))
        return result
        
        
        