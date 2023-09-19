#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
dfs 判断node的子结点是否能添加到结果中去 如果是叶结点 并且总和为target则加入到结果中
"""
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        if root and not root.left and not root.right and root.val==sum:
            return [[root.val]]
        return self.dfs(root,[],root.val,sum,[root.val])
    def dfs(self,node,res,current_sum,target,path):
        for n in [node.left,node.right]:
            if n:
                if self.match(n,current_sum,target):
                    res.append(path+[n.val])
                else:
                    self.dfs(n,res,current_sum+n.val,target,path+[n.val])
        return res
    def match(self,node,current_sum,target):
        if not node.left and not node.right and current_sum+node.val==target:
            return True
        else:
            return False


