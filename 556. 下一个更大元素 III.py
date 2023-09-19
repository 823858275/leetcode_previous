"""
从右往左 找到第一个升序的位置i
然后在i右边从右往左找到第一个大于i的位置j 然后交换i和j（i右边的都是降序）
把i右边的所有元素倒序
"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = list(str(n))
        if len(num) <= 1:
            return -1
        for i in range(len(num) - 1, 0, -1):
            if num[i] > num[i - 1]:
                break
        if i == 1 and num[i] <= num[i - 1]:
            return -1
        i -= 1
        for j in range(len(num) - 1, i - 1, -1):
            if num[j] > num[i]:
                num[i], num[j] = num[j], num[i]
                break
        num[i + 1:] = num[:i:-1]
        res = int(''.join(num))
        return res if res <= ((1 << 31) - 1) else -1


print(Solution().nextGreaterElement(2147483476))