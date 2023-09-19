# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


"""
bfs
"""


# class Solution:
#     def levelOrder(self, root: 'Node') -> List[List[int]]:
#         if not root:
#             return []
#         queue = [root]
#         res = []
#         while queue:
#             size = len(queue)
#             level = []
#             for i in range(size):
#                 node = queue.pop(0)
#                 if node.children:
#                     queue.extend(node.children)
#                 level.append(node.val)
#             res.append(level)
#         return res
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def dfs(node, level):
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            for child in node.children:
                dfs(child, level + 1)

        res = []
        if root:
            dfs(root, 0)
        return res
