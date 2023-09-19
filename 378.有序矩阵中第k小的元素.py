#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row=len(matrix)
        col=len(matrix[0])
        left=matrix[0][0]           # left为矩阵中最小的数，right为矩阵中最大的数，取left、right中间的数为目标值
        right=matrix[row-1][col-1]  # cnt为矩阵matrix中小于等于mid值的个数
        while left<right:
            mid=left+(right-left)//2
            cnt=self.searchLessEqual(matrix,mid)
            if cnt<k:
                left=mid+1
            else:
                right=mid
        return right
    def searchLessEqual(self,matrix,target):
        i=len(matrix)-1#从左下角开始比较
        j=0
        res=0
        while i>=0 and j<len(matrix[0]):
            if matrix[i][j]<=target:
                res+=i+1
                j+=1
            else:
                i-=1
        return res
        

