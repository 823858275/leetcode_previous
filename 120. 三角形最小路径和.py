from typing import List

# 二维dp[i][j]表示到三角形i j位置处的最小路径
# 与dp[i][j] dp[i][j-1] 相关 同时要考虑到最左边和最右边的两个特殊情况
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * len(triangle)
        for i in range(len(triangle)):
            for j in range(len(triangle[i]) - 1, -1, -1):
                if j == 0:
                    dp[j] = dp[j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[j] = triangle[i][j] + dp[j - 1]
                else:
                    dp[j] = min(dp[j] + triangle[i][j], dp[j - 1] + triangle[i][j])
        return min(dp)
