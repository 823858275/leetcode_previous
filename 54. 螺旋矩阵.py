import math
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        circle = min(math.ceil(len(matrix) / 2), math.ceil(len(matrix[0]) / 2))
        res = []
        for i in range(circle):
            res.extend(matrix[i][i:len(matrix[0]) - i])
            for j in range(i + 1, len(matrix) - i):
                res.append(matrix[j][len(matrix[0]) - i - 1])
            for j in range(len(matrix[0]) - i - 2, i - 1, -1):
                if (len(matrix) - i - 1) != i:
                    res.append(matrix[len(matrix) - i - 1][j])
            for j in range(len(matrix) - i - 2, i, -1):
                if i != len(matrix[0]) - i - 1:
                    res.append(matrix[j][i])
        return res
