# Definition for a binary tree node.
# !/usr/bin/env python
# coding=utf-8
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
递归
"""
# class Solution:
#     def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
#         def construct(left, right):
#             if left > right:
#                 return None
#             val = max(nums[left:right+1])
#             max_index = nums.index(val)
#             root = TreeNode(val)
#             root.left = construct(left, max_index - 1)
#             root.right = construct(max_index + 1, right)
#             return root
#
#         return construct(0, len(nums) - 1)
#
# print(Solution().constructMaximumBinaryTree([3,2,1,6,0,5]))

"""
单调栈
栈内保存的节点依次减小，遍历没一个节点，找寻节点的父节点
[3,2,1,6,0,5]
先存3 2 1
由于6>1，1弹出来，在6，2中找1的父节点，2较小所以作1的父节点
然后2弹出来，在6，3中找2的的父节点，3较小所以做1的父节点
"""


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        stack = []
        for num in nums:
            curNode = TreeNode(num)
            while stack and stack[-1].val < num:
                top = stack.pop()
                if stack and stack[-1].val < num:
                    stack[-1].right = top
                else:
                    curNode.left = top
            stack.append(curNode)
        while stack:
            top = stack.pop()
            if stack:
                stack[-1].right = top
        return top

print(Solution().constructMaximumBinaryTree([3,2,1,6,0,5]))