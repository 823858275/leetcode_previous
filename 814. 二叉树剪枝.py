# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def contain1(node):
            if not node:
                return 0
            if not contain1(node.left):
                node.left=None
            if not contain1(node.right):
                node.right=None
            return node.val==1 or contain1(node.left) or contain1(node.right)
        contain1(root)
        return root if contain1(root) else None
