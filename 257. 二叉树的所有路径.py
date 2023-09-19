# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        def dfs(node, path):
            if not node.left and not node.right:
                path += '->' + str(node.val)
                res.append(path[2:])
                return
            if node.left:
                dfs(node.left, path + '->' + str(node.val))
            if node.right:
                dfs(node.right, path + '->' + str(node.val))

        dfs(root, '')
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


print(Solution().binaryTreePaths(deserialize([-64,12,18,-4,-53,'null',76,'null',-51,'null','null',-93,3,'null',-31,47,'null',3,53,-81,33,4,'null',-51,-44,-60,11,'null','null','null','null',78,'null',-35,-64,26,-81,-31,27,60,74,'null','null',8,-38,47,12,-24,'null',-59,-49,-11,-51,67,'null','null','null','null','null','null','null',-67,'null',-37,-19,10,-55,72,'null','null','null',-70,17,-4,'null','null','null','null','null','null','null',3,80,44,-88,-91,'null',48,-90,-30,'null','null',90,-34,37,'null','null',73,-38,-31,-85,-31,-96,'null','null',-18,67,34,72,'null',-17,-77,'null',56,-65,-88,-53,'null','null','null',-33,86,'null',81,-42,'null','null',98,-40,70,-26,24,'null','null','null','null',92,72,-27,'null','null','null','null','null','null',-67,'null','null','null','null','null','null','null',-54,-66,-36,'null',-72,'null','null',43,'null','null','null',-92,-1,-98,'null','null','null','null','null','null','null',39,-84,'null','null','null','null','null','null','null','null','null','null','null','null','null',-93,'null','null','null',98])))
