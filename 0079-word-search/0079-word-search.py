from typing import List

class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.board = [[]]

    def dfs(cls, r, c, w, visited, rows, cols, board):
        if w == "":
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != w[0] or (r, c) in visited:
            return False
        else:
            visited.add((r, c))
            result = (
                cls.dfs(r + 1, c, w[1:], visited, rows, cols, board) or
                cls.dfs(r - 1, c, w[1:], visited, rows, cols, board) or
                cls.dfs(r, c + 1, w[1:], visited, rows, cols, board) or
                cls.dfs(r, c - 1, w[1:], visited, rows, cols, board)
            )
            visited.remove((r, c))
            return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        for r in range(self.rows):
            for c in range(self.cols):
                visited = set()
                if self.board[r][c] == word[0] and self.dfs(r, c, word, visited, self.rows, self.cols, self.board):
                    return True
        return False

