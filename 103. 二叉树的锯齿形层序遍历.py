from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# bfs
# 使用is_even判断是否是偶数行
# 奇数行把结果翻转
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        is_even = True
        while queue:
            size = len(queue)
            tmp = []
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                tmp.append(node.val)
            if is_even:
                res.append(tmp)
            else:
                res.append(list(reversed(tmp)))
            is_even = not is_even
        return res
