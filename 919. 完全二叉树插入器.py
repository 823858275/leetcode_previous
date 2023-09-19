# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.dic = {}
        n = 0
        queue = [root]
        while queue:
            n += 1
            node = queue.pop(0)
            self.dic[n] = node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, v: int) -> int:
        i = len(self.dic) + 1
        self.dic[i] = TreeNode(v)
        parent = self.dic[i // 2]
        if i % 2 == 0:
            parent.left = self.dic[i]
        else:
            parent.right = self.dic[i]
        return parent.val

    def get_root(self) -> TreeNode:
        return self.dic[1]

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
