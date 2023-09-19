from typing import List

"""
从左下角或者右上角开始选
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        row = len(matrix)
        col = len(matrix[0])
        i, j = row - 1, 0
        while 0 <= i < row and 0 <= j < col:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return True
        return False
