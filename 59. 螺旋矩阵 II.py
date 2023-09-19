import math

from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        circle = math.ceil(n / 2)
        res = [[0] * n for i in range(n)]
        count = 1
        for i in range(circle):
            row = col = i
            for col in range(i,n-i):
                res[row][col] = count
                count += 1
            for row in range(i+1,n-i):
                res[row][col] = count
                count += 1
            for col in range(n-i-2,i-1,-1):
                res[row][col] = count
                count += 1
            for row in range(n - i - 2, i, -1):
                res[row][col] = count
                count += 1
        return res
