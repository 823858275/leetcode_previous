from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        blank = []
        valid = False
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    blank.append((i, j))
                else:
                    row[i][int(board[i][j]) - 1] = True
                    col[j][int(board[i][j]) - 1] = True
                    block[i // 3][j // 3][int(board[i][j]) - 1] = True

        def dfs(ind):
            nonlocal valid
            if ind == len(blank):
                valid = True
                return
            x, y = blank[ind]
            for i in range(9):
                if row[x][i]==col[y][i]==block[x//3][y//3][i]==False:
                    row[x][i] = col[y][i] = block[x // 3][y // 3][i] = True
                    board[x][y]=str(i+1)
                    dfs(ind+1)
                    row[x][i] = col[y][i] = block[x // 3][y // 3][i] = False
                    if valid:
                        return
        dfs(0)
