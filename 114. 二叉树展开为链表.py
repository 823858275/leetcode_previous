# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 原地算法，对树进行修改
# 关键点是对树的左子树进行修改，需要把树的左子树移到右子树
# 但是在移动过去的时候要考虑右子树放哪边
# 因为是前序遍历，所以右子树应该放在左子树往右深入到底，然后放在这个节点的右边
# 然后把左子树放到右边
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        curNode = root
        while curNode:
            if curNode.left:
                preNode = curNode.left
                while preNode.right:
                    preNode = preNode.right
                preNode.right = curNode.right
                curNode.right = curNode.left
                curNode.left = None
            curNode = curNode.right
