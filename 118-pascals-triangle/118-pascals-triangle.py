class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(0, i - 1):
                row.append(result[-1][j] + result[-1][j+1])
            
            row.append(1)
            result.append(row)
        return result

            