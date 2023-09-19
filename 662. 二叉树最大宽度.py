# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
层次遍历：
某一层记录节点的位置pos，则它左节点的位置为pos*2，右结点的位置为pos*2+1
"""


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(root, 0)]
        res = 0
        while queue:
            size = len(queue)
            res = max(res, queue[size - 1][1] - queue[0][1] + 1)
            for i in range(size):
                node, pos = queue.pop(0)
                if node.left:
                    queue.append((node.left, pos * 2))
                if node.right:
                    queue.append((node.right, pos * 2 + 1))
        return res
