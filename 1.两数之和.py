#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        res=[]
        for i in range(len(nums)):
            if dic.get(target-nums[i])!=None:
                res.append(dic[target-nums[i]])
                res.append(i)
                break
            dic[nums[i]]=i
        return res
