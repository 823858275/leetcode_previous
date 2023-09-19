# 26进制
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            res += 26 ** (len(columnTitle) - i - 1)*(ord(columnTitle[i])-ord('A')+1)
        return res
print(Solution().titleToNumber('AB'))