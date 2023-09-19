from typing import List
"""
dp[i][j] 以坐标i j 为右下角能形成的正方形的边长
由该坐标的左边、上面、左上角正方形决定当前位置的边长
"""
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         if len(matrix) == 0 or len(matrix[0]) == 0:
#             return 0
#         maxSide = 0
#         row, col = len(matrix), len(matrix[0])
#         dp = [[0] * col for _ in range(row)]
#         for i in range(row):
#             for j in range(col):
#                 if matrix[i][j] == '1':
#                     if i == 0 or j == 0:
#                         dp[i][j] = 1
#                     else:
#                         dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
#                     maxSide = max(maxSide, dp[i][j])
#         return maxSide * maxSide


"""
二维压缩成一维
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        maxSide = 0
        row, col = len(matrix), len(matrix[0])
        dp = [0] * col
        for i in range(row):
            pre = 1
            for j in range(col):
                if matrix[i][j] == '1':
                    tmp = dp[j]
                    if i == 0 or j == 0:
                        dp[j] = 1
                    else:
                        dp[j] = min(pre, dp[j - 1], dp[j]) + 1
                    pre = tmp
                    maxSide = max(maxSide, dp[j])
                else:
                    dp[j] = 0
        return maxSide * maxSide