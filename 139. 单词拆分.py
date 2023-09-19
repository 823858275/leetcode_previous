# dp[i]表示s前面i个元素是否正确
# 遍历i：遍历j：判断i位置后面的元素是否在词典中
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            for j in range(i + 1, len(s) + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]