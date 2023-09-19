# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 想要平衡的话，根节点必须取中间一个数
# 当数组为奇数个，直接取中间，如果为偶数个，可取中间左右任一个
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            root = TreeNode(nums[(left + right) // 2])
            root.left = helper(left, (left + right) // 2 - 1)
            root.right = helper((left + right) // 2 + 1, right)
            return root

        return helper(0, len(nums) - 1)
