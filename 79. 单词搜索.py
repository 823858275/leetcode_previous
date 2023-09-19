from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(res, ind, i, j, visited):
            if res == word:
                return True
            if ind >= len(word):
                return False
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if 0 <= i + dx < len(board) and 0 <= j + dy < len(board[0]):
                    if board[i + dx][j + dy] == word[ind] and visited[i + dx][j + dy] != 1:
                        visited[i + dx][j + dy] = 1
                        ans = dfs(res + board[i + dx][j + dy], ind + 1, i + dx, j + dy, visited)
                        if ans:
                            return ans
                        visited[i + dx][j + dy] = 0
            return False

        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = [[0] * len(board[0]) for i in range(len(board))]
                    visited[i][j] = 1
                    res = dfs(word[0], 1, i, j, visited)
                    if res:
                        return res
        return res


print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"))
