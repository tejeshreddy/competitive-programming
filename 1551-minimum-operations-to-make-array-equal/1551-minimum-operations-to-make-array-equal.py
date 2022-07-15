class Solution:
    def minOperations(self, n: int) -> int:
        l, r = 0, n - 1
        
        result = 0
        arr = [2 * i + 1 for i in range(n)]
        mean = sum(arr) / len(arr)
        
        result = 0
        for i in arr:
            result += abs(i - mean)
        return int(result // 2)
            
        
        
