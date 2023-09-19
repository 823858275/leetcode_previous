#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=1
        right=1
        res=[]
        for i in range(len(nums)):
            res.append(left)
            left*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i]*=right
            right*=nums[i]
        return res
