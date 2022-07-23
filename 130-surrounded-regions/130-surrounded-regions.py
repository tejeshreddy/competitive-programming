class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, current_value, change_value):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != current_value:
                return
            board[r][c] = change_value
            dfs(r + 1, c, current_value, change_value)
            dfs(r - 1, c, current_value, change_value)
            dfs(r, c + 1, current_value, change_value)
            dfs(r, c - 1, current_value, change_value)
                
        
        for r in [0, rows - 1]:
            for c in range(cols):
                dfs(r, c, "O", "#")
        
        for c in [0, cols - 1]:
            for r in range(rows):
                print(r, c)
                dfs(r, c, "O", "#")
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    dfs(r, c, "O", "X")
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"
        
            