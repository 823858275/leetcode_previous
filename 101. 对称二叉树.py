# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
递归：dfs 判断某个树的左右子树是否是镜像的
终止条件：两个节点都空（True），两个节点一个空一个不空（False），两个节点的值不一样（False）
每次递归的时候判断左右，右左是否成立
"""
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         def dfs(node1,node2):
#             if not node1 and not node2:
#                 return True
#             if not node1 or not node2:
#                 return False
#             if node1.val!=node2.val:
#                 return False
#             return dfs(node1.left,node2.right) and dfs(node1.right,node2.left)
#         return dfs(root.left,root.right)

"""
队列，也是左右、右左依次入列
"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True
        queue = [root.left, root.right]
        while queue:
            size = len(queue)
            for i in range(0, size, 2):
                node1, node2 = queue.pop(0), queue.pop(0)
                if not node1 and not node2:
                    continue
                if not node1 or not node2:
                    return False
                if node1.val != node2.val:
                    return False
                queue.append(node1.left)
                queue.append(node2.right)
                queue.append(node1.right)
                queue.append(node2.left)
        return True
