from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if grid[row][col] == 0:
                return 0
            area = 1
            grid[row][col] = 0
            for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if 0 <= (row + i) < len(grid) and 0 <= (col + j) < len(grid[0]):
                    area += dfs(row + i, col + j)
            return area

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(dfs(i, j), res)
        return res
