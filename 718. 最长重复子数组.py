from typing import List


# 滑动窗口
# 将两个数组想象成尺，从头开始相交，然后遍历每段的最大窗口长度
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n, m = len(A), len(B)
        res = 0
        for i in range(n):
            length = min(n - i, m)
            res = max(self.maxWindow(A, B, i, 0, length, res), res)
        for i in range(m):
            length = min(m - i, n)
            res = max(self.maxWindow(A, B, 0, i, length, res), res)
        return res

    def maxWindow(self, A, B, addA, addB, length, res):
        k = 0
        if length > res:
            for i in range(length):
                if k + length - i <= res:
                    break
                if A[addA + i] == B[addB + i]:
                    k += 1
                else:
                    res = max(res, k)
                    k = 0
        res = max(res, k)
        return res


print(Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
