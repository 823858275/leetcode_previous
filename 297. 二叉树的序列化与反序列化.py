# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
dfs，前序遍历
"""
# class Codec:
#
#     def serialize(self, root):
#         """Encodes a tree to a single string.
#
#         :type root: TreeNode
#         :rtype: str
#         """
#         if not root:
#             return 'x,'
#         left = self.serialize(root.left)
#         right = self.serialize(root.right)
#         return str(root.val) + ',' + left + right
#
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
#
#         :type data: str
#         :rtype: TreeNode
#         """
#         data=data.split(',')
#         return self.buildTree(data)
#     def buildTree(self,data):
#         val=data.pop(0)
#         if val=='x':
#             return None
#         root=TreeNode(int(val))
#         root.left=self.buildTree(data)
#         root.right=self.buildTree(data)
#         return root

"""
层序遍历bfs
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = [root]
        res = ''
        while queue:
            node = queue.pop(0)
            if node:
                res += str(node.val) + ','
                queue.append(node.left)
                queue.append(node.right)
            else:
                res += 'x,'
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        root = TreeNode(int(data.pop(0)))
        queue = [root]
        while queue:
            node = queue.pop(0)
            if data:
                val = data.pop(0)
                if val != 'x':
                    node.left = TreeNode(int(val))
                    queue.append(node.left)
            if data:
                val = data.pop(0)
                if val != 'x':
                    node.right = TreeNode(int(val))
                    queue.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
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

print(Codec().serialize(deserialize([1,2,3,'null','null',4,5])))