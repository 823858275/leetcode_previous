# 十进制转十六进制，先转为2进制，然后再转为16进制
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        res = ''
        s = '0123456789abcdef'
        while num:
            res = s[num & 15] + res
            num >>= 4
            if len(res) >= 8:
                return res
        return res


print(Solution().toHex(-20))
