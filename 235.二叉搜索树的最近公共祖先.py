#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#最近的公共祖先结点的值在两个结点值之间
#如果当前结点的值小于较小值则往右子树中寻找
#如果当前结点的值大于较大值则往左子树中寻找
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pa=min(p.val,q.val)
        pb=max(p.val,q.val)
        return self.findNode(root,pa,pb)
    def findNode(self,node: TreeNode,a: int,b: int):
        if not node:
            return None
        tmp=node.val
        if tmp>=a and tmp<=b:
            return node
        elif tmp<a:
            return self.findNode(node.right,a,b)
        elif tmp>b:
            return self.findNode(node.left,a,b)

