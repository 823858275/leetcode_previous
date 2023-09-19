# 模拟除法，每一步除下来都有余数和商，当余数出现以前出现过的时候就会循环
# 首先判断正负
# 然后一步步计算商和余数
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = []
        if numerator == 0:
            return '0'
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        a, remind = divmod(numerator, denominator)
        res.append(str(a))
        if remind == 0:
            return ''.join(res)
        res.append('.')
        dic = {}
        while remind != 0:
            if remind in dic:
                res.insert(dic[remind], '(')
                res.append(')')
                break
            dic[remind] = len(res)
            a, remind = divmod(remind * 10, denominator)
            res.append(str(a))
        return ''.join(res)

print(Solution().fractionToDecimal(-50,8))