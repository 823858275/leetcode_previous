# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



"""
中序遍历 每次比较当前节点与前一个节点的大小
"""

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        node, stack, pre_value = root, [], float('-inf')
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val <= pre_value:
                return False
            else:
                pre_value = node.val
            node = node.right
        return True
