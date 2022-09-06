class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, w):
            if w == "":
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != w[0] or (r, c) in visited:
                return False
            else:
                visited.add((r, c))
                result = dfs(r + 1, c, w[1:]) or dfs(r - 1, c, w[1:]) or dfs(r, c + 1, w[1:]) or dfs(r, c - 1, w[1:])
                visited.remove((r, c))
                return result
        
        for r in range(0, rows):
            
            for c in range(0, cols):
                visited = set()
                if board[r][c] == word[0] and dfs(r, c, word):
                    return True
        return False
                    
                
            
            