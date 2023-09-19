# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 根右左 -> 左右根
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, node, res = [], root, []
        while stack or node:
            while node:
                stack.append(node)
                res.append(node.val)
                node = node.right  # 这里和下面交换了原版先序的顺序
            node = stack.pop()
            node = node.left  # 这里和上面交换了原版先序的顺序
        return reversed(res)
