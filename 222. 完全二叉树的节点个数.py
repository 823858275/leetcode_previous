# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
先求出节点的深度h（0开始），如果最后一层只有一个节点则总节点数为2^h，如果最后一层满节点
则总节点数为2^(h+1)-1
最后通过二分查找，判断一个节点是否存在。
通过位与的方法，例如12的二进制为1100，则从根节点出发玩右、左、左走到12
"""
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        level = 0
        node = root
        while node.left:
            level += 1
            node = node.left
        left, right = 1 << level, (1 << (level + 1))
        while left < right-1:
            mid = left + (right - left) // 2
            if self.exist(root, level, mid):
                left = mid
            else:
                right = mid
        return left

    def exist(self, node, level, k):
        bit = 1 << (level - 1)
        while node and bit > 0:
            if bit & k:
                node = node.right
            else:
                node = node.left
            bit >>= 1
        return node is not None


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


print(Solution().countNodes(deserialize([1, 2, 3])))
