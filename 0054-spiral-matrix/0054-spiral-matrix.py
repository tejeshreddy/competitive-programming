class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r, t, d = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        result = []
        
        while l <= r and t <= d:
            
            for i in range(l, r + 1):
                result.append(matrix[t][i])
            t += 1
            if t > d: break
            
            for i in range(t, d + 1):
                result.append(matrix[i][r])
            r -= 1
            if r < l: break
            
            for i in range(r, l - 1, -1):
                result.append(matrix[d][i])
            d -= 1
            if d < t: break
            
            for i in range(d, t - 1, - 1):
                result.append(matrix[i][l])
            l += 1
            if l > t: break
        
        return result
        