# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
用一个栈存放左节点
初始化时，把所有左节点放在栈里
调用next的时候，弹出栈顶元素，然后判断是否有右节点，然后找右节点的最左子节点
相当于找下一个小的节点
"""
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._left_most(root)

    def _left_most(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self._left_most(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
