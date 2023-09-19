from typing import List


# 单调栈，stack内存的元素单调不增
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        # 第一步循环，求nums里面前几个元素的结果然后栈顶元素
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        # 第二步循环给nums后面的元素求结果
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
        return res