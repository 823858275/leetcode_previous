# 顺序写入 注意边界条件
class Solution:
    def myAtoi(self, s: str) -> int:
        bound_up = (1 << 31) - 1
        n = len(s)
        ind = 0
        # 去掉开头的空格
        while ind < n and s[ind] == ' ':
            ind += 1
        # 如果是'            '这种情况
        if ind == n:
            return 0
        # 判断首字母是否为正负号
        sign = 1
        first = s[ind]
        if first == '+':
            ind += 1
        elif first == '-':
            ind += 1
            sign = -1
        res = 0
        while ind < n:
            cur = s[ind]
            # 非数字直接中断
            if cur > '9' or cur < '0':
                break
            # 超出上界
            if res > bound_up // 10 or (res == bound_up // 10 and cur > str(bound_up % 10)):
                return bound_up
            # 低于下界
            if res < -(bound_up // 10) or (res == -(bound_up // 10) and cur > str((bound_up + 1) % 10)):
                return -bound_up - 1
            res = res * 10 + sign * int(cur)
            ind += 1
        return res


print(Solution().myAtoi("  -a0012a42"))
