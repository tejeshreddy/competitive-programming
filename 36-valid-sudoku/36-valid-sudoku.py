class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        visited = set()
        rows, cols = len(board), len(board[0])        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                s1 = str(board[r][c]) + " in row " + str(r)
                s2 = str(board[r][c]) + " in col " + str(c)
                s3 = str(board[r][c]) + " in grid " + str(c // 3) + " - " + str(r // 3)
                # print(s1, s2, s3)
                if s1 in visited or s2 in visited or s3 in visited:
                    return False
                else:
                    visited.add(s1)
                    visited.add(s2)
                    visited.add(s3)
        return True