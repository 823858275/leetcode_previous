# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 先找到要删除的节点
# 如果是叶节点就直接置为None
# 否则如果有左节点找前驱节点，如果有右结点则找后继节点
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                node=root.right
                while node.left and node.left.left:
                    node=node.left
                root.val = node.left.val
                node.left=None
            else:
                node=root.left
                while node.right and node.right.right:
                    node=node.right
                root.val = node.right.val
                node.right=None
        return root

    def successor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def predecessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.val
