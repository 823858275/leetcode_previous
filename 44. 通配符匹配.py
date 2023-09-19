# 二维dp，dp[i][j]表示s前i个字符，p前j个字符，这时是否匹配
# 对于某个i，j
# 分s[i]，p[j]相等，p[j]为'?'，p[j]为'*'三种情况，情况1和情况2可以合并
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(0, len(p)):
            if p[j] == '*':
                dp[0][j + 1] = True
            else:
                break
        for i in range(len(s)):
            for j in range(len(p)):
                if s[i] == p[j] or p[j] == '?':
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == '*':
                    dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1]
        return dp[len(s)][len(p)]


print(Solution().isMatch('aa', 'a'))
