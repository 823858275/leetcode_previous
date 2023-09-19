# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
dp[0] 表示当前节点不偷时能获得的最大值 （当前节点不偷 左节点右节点可偷可不偷 取最大值）
dp[1] 表示当前节点偷能获得的最大值（当前节点偷 左结点右结点都不偷）
后序遍历
"""
class Solution:
    def rob(self, root: TreeNode) -> int:
        res = self.dfs(root)
        return max(res[0], res[1])

    def dfs(self, node):
        if node is None:
            return [0, 0]

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        dp = [0, 0]
        # dp[0]表示以当前节点不偷状态下子树能够偷取的最大值,注意当前节点不偷的话，它的子树可以偷也可以不偷
        dp[0] = max(left[0], left[1]) + max(right[0], right[1])
        # dp[1]表示当前节点偷状态下子树能够偷取的最大值
        dp[1] = node.val + left[0] + right[0]
        return dp
