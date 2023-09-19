# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            root_index = inorder_index[val]
            root.right = helper(root_index + 1, in_right)
            root.left = helper(in_left, root_index - 1)
            return root

        inorder_index = {val: i for i, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
