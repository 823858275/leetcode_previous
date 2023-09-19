# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
中序遍历的逆遍历，右根左
"""


# class Solution:
#     def convertBST(self, root: TreeNode) -> TreeNode:
#         total = 0
#
#         def dfs(node):
#             nonlocal total
#             if not node:
#                 return
#             dfs(node.right)
#             total += node.val
#             node.val = total
#             dfs(node.left)
#
#         dfs(root)
#         return root
"""
moris反向中序遍历
"""
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        total = 0
        node = root
        while node:
            if node.right:
                preNode = node.right
                while preNode.left and preNode.left != node:
                    preNode = preNode.left
                if not preNode.left:
                    preNode.left = node
                    node = node.right
                else:
                    total += node.val
                    preNode.left = None
                    node.val = total
                    node = node.left
            else:
                total += node.val
                node.val = total
                node = node.left
        return root
def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    if not data:
        return None
    root = TreeNode(data.pop(0))
    queue = [root]
    while queue:
        node = queue.pop(0)
        if data:
            val = data.pop(0)
            if val != 'null':
                node.left = TreeNode(val)
                queue.append(node.left)
        if data:
            val = data.pop(0)
            if val != 'null':
                node.right = TreeNode(val)
                queue.append(node.right)
    return root
print(Solution().convertBST(deserialize([4,1,6,0,2,5,7,'null','null','null',3,'null','null','null',8])))
