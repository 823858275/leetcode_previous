#dp
#用dp[i]表示s[0:i]的最终结果
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or int(s[0]) == 0:
            return 0
        pre, cur = 1, 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i - 1] in ['1', '2']:
                    tmp=cur
                    cur=pre
                    pre=tmp
                else:
                    return 0
            else:
                if s[i - 1] == '1':
                    tmp = cur
                    cur = pre + cur
                    pre = tmp
                elif s[i - 1] == '2':
                    if 0 <= int(s[i]) <= 6:
                        tmp = cur
                        cur = pre + cur
                        pre = tmp
                    else:
                        pre = cur
                else:
                    pre = cur
        return cur


print(Solution().numDecodings("01"))
