# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res, pre = float('inf'), float('-inf')

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal res, pre
            res = min(res, abs(node.val - pre))
            pre = node.val
            dfs(node.right)

        dfs(root)
        return res
