# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
编码后续遍历，则编码之后为左右根
解码由于采用栈，先弹出来的是根，然后是右，左
"""


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def postorder(node):
            return postorder(node.left) + postorder(node.right) + [node.val] if node else []

        return ' '.join(map(str, postorder(root)))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        def help(low, high):
            if not data or data[-1] < low or data[-1] > high:
                return None
            val = data.pop()
            root = TreeNode(val)
            root.right = help(val, high)
            root.left = help(low, val)
            return root

        data = [int(x) for x in data.split(' ') if x]
        return help(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
