class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtracking(temp, target, start, end):
            if target < 0:
                return
            if target == 0 and temp[:] not in result:
                result.append(temp[:])
                
            for i in range(start, end):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                temp.append(candidates[i])
                backtracking(temp, target - candidates[i], i + 1, end)
                temp.pop()
        candidates.sort()
        result = []
        backtracking([], target, 0, len(candidates))
        return result
        