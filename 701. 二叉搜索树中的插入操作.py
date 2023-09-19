# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
最终结果插入到叶结点，如果小了，找左节点，如果大了找右结点
"""
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        node = root
        while node:
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
        return root
