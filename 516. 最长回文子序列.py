"""
dp[i][j]表示从索引i到j的最长回文子序列
初始情况：对角线即i==j，字符串只有一个字符，dp为1
对于i,j，如果两个相等，则往里一格+2
不等就左右各自往里一格，取较大
"""


# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         size = len(s)
#         dp = [[0] * size for _ in range(size)]
#         0
#         for i in range(size):
#             dp[i][i] = 1
#         for i in range(size - 2, -1, -1):
#             for j in range(i + 1, size):
#                 if s[i] == s[j]:
#                     dp[i][j] = dp[i + 1][j - 1] + 2
#                 else:
#                     dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
#         return dp[0][size - 1]

# 二维压缩成一维
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        size = len(s)
        dp = [1] * size
        for i in range(size - 2, -1, -1):
            pre = 0
            for j in range(i + 1, size):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre+2
                else:
                    dp[j] = max(dp[j - 1], dp[j])
                pre = tmp
        return dp[size - 1]
