# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方法一：分治
# 定义helpBuildTree建立指定索引范围内的树
# 先确定根节点，即前序遍历数组第一个位置的节点
# 再确定左右子树长度，然后确定两个数组的索引继续调用helpBuildTree
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helpBuildTree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            root = TreeNode(preorder[preorder_left])
            inorder_root = inorder_index[preorder[preorder_left]]
            left = inorder_root - inorder_left
            right = inorder_right - inorder_root
            root.left = helpBuildTree(preorder_left + 1, preorder_left + left, inorder_left, inorder_root - 1)
            root.right = helpBuildTree(preorder_left + left + 1, preorder_right, inorder_root + 1, inorder_right)
            return root

        inorder_index = {node: i for i, node in enumerate(inorder)}
        return helpBuildTree(0, len(preorder) - 1, 0, len(inorder) - 1)
# 方法二：栈迭代
# 依次遍历前序数组，然后构建树，相当于一直往左深入，直到中序数组的首位
# 相当于到头了，然后把栈内节点弹出，并且中序数组遍历，直到两者值不一样，说明到了右节点
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         if not preorder:
#             return None
#
#         root = TreeNode(preorder[0])
#         stack = [root]
#         inorderIndex = 0
#         for i in range(1, len(preorder)):
#             preorderVal = preorder[i]
#             node = stack[-1]
#             if node.val != inorder[inorderIndex]:
#                 node.left = TreeNode(preorderVal)
#                 stack.append(node.left)
#             else:
#                 while stack and stack[-1].val == inorder[inorderIndex]:
#                     node = stack.pop()
#                     inorderIndex += 1
#                 node.right = TreeNode(preorderVal)
#                 stack.append(node.right)
#
#         return root
