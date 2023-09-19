"""
dp[i][j]表示从索引i到j，至少需要插入几次
"""


# class Solution:
#     def minInsertions(self, s: str) -> int:
#         size = len(s)
#         dp = [[0] * size for _ in range(size)]
#         for i in range(size - 1, -1, -1):
#             for j in range(i + 1, size):
#                 if s[i] == s[j]:
#                     dp[i][j] = dp[i + 1][j - 1]
#                 else:
#                     dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
#         return dp[0][size - 1]


class Solution:
    def minInsertions(self, s: str) -> int:
        size = len(s)
        dp = [0] * size
        for i in range(size - 1, -1, -1):
            pre = 0
            for j in range(i + 1, size):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + 1
                pre = tmp
        return dp[size - 1]


print(Solution().minInsertions("mbadm"))
