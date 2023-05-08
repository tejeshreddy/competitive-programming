class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        dim = len(mat)
        result = 0
        
        for i in range(dim):
            result += mat[i][i]
            result += mat[i][dim - i - 1]
        if dim % 2 == 1:
            return result -mat[dim//2][dim//2]
        return result
            
        