from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        ans = [['.'] * n for _ in range(n)]

        def dfs(row):
            if row == n:
                res.append([])
                for line in ans:
                    line = ''.join(line)
                    res[-1].append(line)
                return
            for col in range(n):
                if valid(row, col):
                    ans[row][col] = 'Q'
                    dfs(row + 1)
                    ans[row][col] = '.'

        def valid(row, col):
            for i in range(row):
                if ans[i][col] == 'Q':
                    return False
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if ans[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if ans[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        dfs(0)
        return res


print(Solution().solveNQueens(4))
