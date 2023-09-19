from typing import List
import math


# 杨辉三角第n行第m列的元素（都是从0开始计数）值为Cm,n
# 则第n行第m列的元素为Cm,n=Cm-1,n * (n-m+1)/m
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(1, math.ceil((rowIndex + 1) / 2)):
            res.append(int(res[-1] * (rowIndex - i + 1) / i))
        return res + res[::-1] if (rowIndex + 1) % 2 == 0 else res + res[-2::-1]


print(Solution().getRow(2))
