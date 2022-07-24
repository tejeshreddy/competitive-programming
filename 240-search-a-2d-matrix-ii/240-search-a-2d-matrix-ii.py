class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h, w = len(matrix), len(matrix[0])
        y, x = h - 1, 0
        
        
        while True:
            
            if y < 0 or x >= w:
                break
            
            current = matrix[y][x]
            
            if target == current:
                return True
            elif target < current:
                y -= 1
            else:
                x += 1

            