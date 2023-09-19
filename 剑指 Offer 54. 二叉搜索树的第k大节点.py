# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
二叉搜索树中序遍历的倒序形成的就是递减数组
然后找第k个数
"""


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res = 0

        def dfs(root):
            if not root:
                return
            dfs(root.right)
            nonlocal k
            if k == 0:
                return
            k -= 1
            if k == 0:
                nonlocal res
                res = root.val
            dfs(root.left)

        dfs(root)
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


print(Solution().kthLargest(deserialize([5, 3, 6, 2, 4, 'null', 'null', 1]), 3))
