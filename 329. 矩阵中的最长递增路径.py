from typing import List
import collections


# 有向图中寻找最长路径
# 记忆化dfs，记忆化指保存中间结果
# dfs(i,j)求i，j点的最长递增路径
# 用store保存中间结果
# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         if not matrix:
#             return 0
#         row, col = len(matrix), len(matrix[0])
#         store = [[0] * col for i in range(row)]
#         res = 0
#
#         def dfs(i, j):
#             nonlocal res
#             compare = []
#             for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
#                 if 0 <= i + dx < row and 0 <= j + dy < col and matrix[i + dx][j + dy] < matrix[i][j]:
#                     compare.append(store[i + dx][j + dy]) if store[i + dx][j + dy] else compare.append(dfs(i+dx, j+dy))
#             store[i][j] = max(compare) + 1 if compare else 1
#             res = max(res, store[i][j])
#             return store[i][j]
#
#         for i in range(row):
#             for j in range(col):
#                 if not store[i][j]:
#                     dfs(i, j)
#         return res

# 拓扑排序
# 先计算每个节点的出度，然后从出度为0的节点往前延伸，延伸到一个节点那个节点的出度就-1，计算最终的层数
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        out_dgree = [[0] * col for i in range(row)]
        deque = collections.deque()
        for i in range(row):
            for j in range(col):
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    if 0 <= i + dx < row and 0 <= j + dy < col and matrix[i + dx][j + dy] > matrix[i][j]:
                        out_dgree[i][j] += 1
                if out_dgree[i][j] == 0:
                    deque.append((i, j))
        ans = 0
        while deque:
            ans += 1
            length = len(deque)
            for _ in range(length):
                i, j = deque.popleft()
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    if 0 <= i + dx < row and 0 <= j + dy < col and matrix[i + dx][j + dy] < matrix[i][j]:
                        out_dgree[i + dx][j + dy] -= 1
                        if out_dgree[i + dx][j + dy] == 0:
                            deque.append((i + dx, j + dy))
        return ans


print(Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
