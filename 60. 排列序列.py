"""
首先确定排列中的第一个数a1
以1为开头有(n-1)!个排列
以2为开头有(n-1)!个排列
。。。
根据k的值应当选取k // (n - 1)! + 1作为首个值
然后对于第二个数的选取
以1为开头有(n-2)!个排列
则k'=k // (n - 2)! + 1
然后依次类推
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]  # 用于保存计算出的阶乘
        for i in range(1, n):
            factorial.append(factorial[-1] * i)

        k -= 1
        ans = list()
        valid = [1] * (n + 1)  # 判断某个元素是否用过
        for i in range(1, n + 1):
            order = k // factorial[n - i] + 1  # 第几个
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    ans.append(str(j))
                    valid[j] = 0
                    break
            k %= factorial[n - i]  # 更新k

        return "".join(ans)

print(Solution().getPermutation(3,3))