# Definition for a binary tree node.
from typing import List


# 右视图优先把左结点加入栈中，同时保存深度（先进后出），则弹出栈时优先考虑右结点
# 当深度比当前最大深度要大，存入字典中
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        right_node = {0: root.val}
        max_depth = 0
        stack = [(0, root)]
        while stack:
            depth, node = stack.pop()
            if depth > max_depth:
                max_depth = depth
                right_node[depth] = node.val
            if node.left:
                stack.append((depth + 1, node.left))
            if node.right:
                stack.append((depth + 1, node.right))
        return [right_node[i] for i in range(max_depth + 1)]
