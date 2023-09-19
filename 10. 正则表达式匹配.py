# 二维dp，dp[i][j]表示s前i个字符，p前j个字符，这时是否匹配
# 对于某个i，j
# 分为两种情况：1、p[j]不为'*'，判断s[i]与p[j]匹配，考虑s前i-1个字符，p前j-1个字符的情况
# 2、p[j]为'*'
# 如果s[i]与p[j-1]匹配，则分两种情况：1、p *取0个前面的字符 2、 取多个前面的字符
# 如果不匹配，则p的 * 表示取0个字符
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n, 2):
            if p[j] == '*':
                dp[0][j + 1] = True
            else:
                break
        for i in range(m):
            for j in range(n):
                if s[i] == p[j] or p[j] == '.':
                    dp[i + 1][j + 1] = dp[i][j]
                if p[j] == '*':
                    if s[i] == p[j - 1] or p[j - 1] == '.':
                        dp[i + 1][j + 1] = dp[i + 1][j - 1] or dp[i][j + 1]
                    else:
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
        return dp[m][n]


print(Solution().isMatch("aab", "c*a*b"))
