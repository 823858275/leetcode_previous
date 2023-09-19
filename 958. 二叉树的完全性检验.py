# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
层序遍历，如果碰到空节点，说明其后续不能有节点了，否则就return False
"""
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        queue = [root]
        reach_end = False
        while queue:
            node = queue.pop(0)
            if reach_end and node:
                return False
            if not node:
                reach_end = True
                continue
            queue.append(node.left)
            queue.append(node.right)
        return True
