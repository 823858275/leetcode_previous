# 将第一个较小的数与后面较大的数交换
# 用last[i]存放0-9每个数字在num中的最后一个位数
# 第一次遍历num，完成last
# 第二次遍历，返回结果
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        last = [-1] * 10
        for i in range(len(s)):
            last[int(s[i])] = i
        for i in range(len(s)):
            for d in range(9, int(s[i]), -1):
                if last[d] > i:
                    return s[:i] + s[last[d]] + s[i + 1:last[d]] + s[i] + s[last[d] + 1:]
        return num


print(Solution().maximumSwap(2736))
