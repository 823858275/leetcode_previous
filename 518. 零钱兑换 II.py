from typing import List
"""
二维dp[i][j] i表示到索引i的硬币 j表示要凑的硬币总数
dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]
索引i的硬币一次都不取 索引i的硬币至少取一次
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1
        if not coins: return 0
        m, n = len(coins), amount
        dp = [[0] * (n + 1) for _ in range(m)]
        # 初始化
        for i in range(m):
            dp[i][0] = 1
        # 迭代
        for i in range(m):
            for j in range(1, n + 1):
                if j >= coins[i]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

"""
二维dp压缩成1维
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if not coins:
            return 0
        m, n = len(coins), amount
        dp = [0] * (n + 1)
        dp[0] = 1
        # 迭代
        for i in range(m):
            for j in range(coins[i], n + 1):
                dp[j] = dp[j] + dp[j - coins[i]]
        return dp[-1]