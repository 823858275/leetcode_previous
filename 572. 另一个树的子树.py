# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# dfs 递归
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def check(node1, node2):
            if not node1 and not node2:
                return True
            if (not node1 or not node2) or node1.val != node2.val:
                return False
            return check(node1.left, node2.left) and check(node1.right, node2.right)

        def dfs(node1, node2):
            if not node1:
                return False
            return check(node1, node2) or dfs(node1.left, node2) or dfs(node1.right, node2)

        return dfs(s, t)


