# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
dfs用于求解某个节点距离target节点的距离
subtree_add用户训练某个节点的子结点中距离为K的节点
对于dfs，如果节点为空节点 返回-1，如果到target节点返回0，然后从target节点深入，寻找距离为K的节点
对于一般节点，首先判断左右子树是否有target，然后在相反节点找距离为K的target
"""


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        ans = []

        # Return distance from node to target if exists, else -1
        # Vertex distance: the # of vertices on the path from node to target
        def dfs(node):
            if not node:
                return -1
            elif node is target:
                # 找出target子结点中距离为K的节点
                subtree_add(node, 0)
                return 0
            else:
                L, R = dfs(node.left), dfs(node.right)
                if L != -1:
                    if L + 1 == K:
                        ans.append(node.val)
                    if L + 1 < K:
                        subtree_add(node.right, L + 2)
                    return L + 1
                elif R != -1:
                    if R + 1 == K:
                        ans.append(node.val)
                    if R + 1 < K:
                        subtree_add(node.left, R + 2)
                    return R + 1
                else:
                    return -1

        # Add all nodes 'K - dist' from the node to answer.
        def subtree_add(node, dist):
            if not node:
                return
            elif dist == K:
                ans.append(node.val)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)

        dfs(root)
        return ans
