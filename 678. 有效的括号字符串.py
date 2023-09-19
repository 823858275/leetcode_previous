"""
贪心
lo表示未配对的左括号的最小值
hi表示未配对的右括号的最大值
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = 0
        hi = 0
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == '*':
                if lo > 0:
                    lo -= 1
                hi += 1
            else:
                if lo > 0:
                    lo -= 1
                hi -= 1
            if hi < 0:
                return False
        return lo == 0
