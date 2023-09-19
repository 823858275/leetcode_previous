# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def helper(pre_left, pre_right, post_left, post_right):
            if pre_left > pre_right:
                return None
            if pre_left == pre_right:
                return TreeNode(pre[pre_left])
            root = TreeNode(pre[pre_left])
            val = pre[pre_left + 1]
            root_index = post_index[val]
            left_length = root_index - post_left + 1
            root.left = helper(pre_left + 1, pre_left + left_length, post_left, root_index)
            root.right = helper(pre_left + 1 + left_length, pre_right, root_index + 1, post_right)
            return root

        post_index = {val: i for i, val in enumerate(post)}
        return helper(0, len(pre) - 1, 0, len(post) - 1)


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
            if val != 'x':
                node.left = TreeNode(val)
                queue.append(node.left)
        if data:
            val = data.pop(0)
            if val != 'x':
                node.right = TreeNode(val)
                queue.append(node.right)
    return root


print(Solution().constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]))
