#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    grid[i][j]=="#"
                    self.dfs(grid,i,j)
                    count+=1
        return count
    def dfs(self, grid, i, j):
        # 遍历可能的子节点
        for k, v in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if self.is_valid(k, v, grid):
                grid[k][v] = '#'
                self.dfs(grid, k, v)

    def is_valid(self, i, j, grid):
        # 如果 i，j 合法的话
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return False
        return True

