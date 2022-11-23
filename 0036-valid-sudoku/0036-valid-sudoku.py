class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        col = set()
        grid = set()
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                rs = str(board[r][c]) + " is in row " + str(r)
                cs = str(board[r][c]) + " is in col " + str(c)
                gs = str(board[r][c]) + " is in grid " + str(r // 3) + "-" + str(c // 3)
                
                if rs in row or cs in col or gs in grid:
                    return False
                row.add(rs)
                col.add(cs)
                grid.add(gs)
                    
        return True
        