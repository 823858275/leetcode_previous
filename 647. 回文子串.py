# Manacher 算法
# dp[i]表示以i为中心的回文子串的半径，即以i为中心能形成几个回文子串
# 对于s，如果回文子串为奇数长度或者偶数长度，中心的个数不唯一，所以往字符串里面插入#
# 在开头和结尾位置用两个不同的字符串$!，用来表示到头了
# dp初始置1，即每个位置至少本身为回文子串
# 设置目前最靠右的回文子串，中点是mid，右端点为right。
# 遍历i，首先判断i是否在回文子串中，在的话min(dp[2 * mid - i], right - i)，即比较和mid中心对称的一个点，以及到右端点的距离
# 相当于利用了之前判断的回文子串，然后继续中心扩散，更新dp
class Solution:
    def countSubstrings(self, s: str) -> int:
        new_s = '$#'
        for c in s:
            new_s += c + '#'
        new_s += '!'
        dp = [1] * len(new_s)
        mid = right = res = 0
        for i in range(1, len(new_s) - 1):
            if i <= right:
                dp[i] = min(dp[2 * mid - i], right - i)
            while new_s[dp[i] + i] == new_s[i - dp[i]]:
                dp[i] += 1
            if i + dp[i] > right:
                mid = i
                right = i + dp[i]
            res += dp[i] // 2
        return res


print(Solution().countSubstrings('aaa'))
