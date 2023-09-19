"""
二维dp[i][j] 表示text1 0-i text2 0-j 的最长公共子序列
"""


# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
#         for i in range(len(text1)):
#             for j in range(len(text2)):
#                 if text1[i]==text2[j]:
#                     dp[i+1][j+1]=dp[i][j]+1
#                 else:
#                     dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
#         return dp[len(text1)][len(text2)]

"""
dp二维转一维
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)
        for i in range(1, len(text1) + 1):
            pre = 0
            for j in range(1, len(text2) + 1):
                tmp = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = pre + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                pre = tmp
        return dp[-1]


print(Solution().longestCommonSubsequence("abcde", "ace"))
