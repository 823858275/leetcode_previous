"""
对于dp[i][j]，表示把word1[0:i]变为word2[0:j]需要的最少操作
举例horse->ros，对于dp[5][3]
对应于i,j位置的两个字符不等
dp[i-1][j]表示hors->ros需要多少操作，然后删除e
dp[i][j-1]表示horse->ro需要多少操作，然后插入s
dp[i-1][j-1]表示hors->ro需要多少操作，然后替换
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
        return dp[-1][-1]
