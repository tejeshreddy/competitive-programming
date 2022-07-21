class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtracking(start, end, tmp):
            result.append(tmp[:])
            for i in range(start, end):
                tmp.append(nums[i])
                backtracking(i + 1, end, tmp)
                tmp.pop()
        
        result = []
        backtracking(0, len(nums), [])
        return result
        