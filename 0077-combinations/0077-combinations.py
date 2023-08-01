class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []
        
        
        def dfs(arr, path):
            if len(path) == k:
                result.append(path)
                return
            
            for i in range(len(arr)):
                dfs(arr[i+1:], path + [arr[i]])
                
        dfs([i for i in range(1, n + 1)], [])
        
        return result
        
            
            
            
        
        
        
        