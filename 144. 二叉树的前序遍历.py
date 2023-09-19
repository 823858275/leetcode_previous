# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res=[]
        node=root
        stack=[]
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node=node.left
            node=stack.pop().right
        return res


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def dfs(root):
            if not root:
                return
            # 按照 左-打印-右的方式遍历
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res