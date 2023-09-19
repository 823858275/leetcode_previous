#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
#方法一

class Solution1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        r=set()
        c=set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    r.add(i)
                    c.add(j)
        for i in range(row):
            for j in range(col):
                if i in r or j in c:
                    matrix[i][j]=0
        

