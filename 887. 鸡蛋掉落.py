# Definition for a binary tree node.
# !/usr/bin/env python
# coding=utf-8
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][1] = i
        for i in range(1, n + 1):
            for j in range(2, k + 1):
                res = float('inf')
                for m in range(1, i + 1):
                    res = min(res, max(dp[m - 1][j - 1], dp[i - m][j]) + 1)
                dp[i][j] = res
        return dp[n][k]


print(Solution().superEggDrop(3, 14))
