class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0] * n for _ in range(n)]
        l, r, u, d = 0, n - 1, 0, n - 1
        
        count = 1
        while l <= r and u <= d:
            for i in range(l, r + 1):
                matrix[u][i] = count
                count += 1
            u += 1
            
            for i in range(u, d + 1):
                matrix[i][r] = count
                count += 1
            r -= 1
            
            for i in range(r, l - 1, -1):
                matrix[d][i] = count
                count += 1
            d -= 1
            
            for i in range(d, u - 1, -1):
                matrix[i][l] = count 
                count += 1
            l += 1
            
        return matrix
            
            
            
            