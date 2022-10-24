class Solution:
    res = 0
    def maxLength(self, arr: List[str]) -> int:
        self.backtracking(arr, 0, "")    
        return self.res
    
    def backtracking(self, arr, ind, string):
        if len(string) != len(set(string)):
            return
        
        self.res = max(self.res, len(string))
        for i in range(ind, len(arr)):
            
            self.backtracking(arr, i + 1, string + arr[i])
            
        
        