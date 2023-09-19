# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, path):
            if not root.left and not root.right:
                nonlocal res
                res += path * 10 + root.val
                return
            if root.left:
                dfs(root.left, path * 10 + root.val)
            if root.right:
                dfs(root.right, path * 10 + root.val)

        dfs(root, 0)
        return res


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


print(Solution().sumNumbers(deserialize([0, 1])))
