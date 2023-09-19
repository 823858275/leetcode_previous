# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
用函数gainMax，表示从一个节点往下，一直往下深入，能够构成的最大路径和
如果是空节点，返回0，如果是叶节点返回叶节点的值。
在递归的同时计算最终结果res，res的值为当前节点的左右两边gainMax
"""


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float('-inf')

        def gainMax(node):
            if not node:
                return 0
            nonlocal res
            leftGain = max(gainMax(node.left), 0)
            rightGain = max(gainMax(node.right), 0)
            maxPath = node.val + leftGain + rightGain
            res = max(res, maxPath)
            return node.val + max(leftGain, rightGain)

        gainMax(root)
        return res
