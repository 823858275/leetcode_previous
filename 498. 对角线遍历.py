from typing import List

"""
确定方向 确定起始
如果向上（下一步是向下） 不在最后一列就向右 否则向下
如果向下（下一步是向上） 不在最后一行就向下 否则向上
"""


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        row, col = len(mat), len(mat[0])
        direction = 1
        res = []
        i, j = 0, 0
        while i < row and j < col:
            while 0 <= i < row and 0 <= j < col:
                res.append(mat[i][j])
                if direction == 1:
                    i -= 1
                    j += 1
                else:
                    i += 1
                    j -= 1
            if direction == 1:
                i += 1
                j -= 1
            else:
                i -= 1
                j += 1
            if direction == 1:
                if j != col - 1:
                    j += 1
                else:
                    i += 1
                direction = 0
            else:
                if i != row - 1:
                    i += 1
                else:
                    j += 1
                direction = 1
        return res


print(Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
