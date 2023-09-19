# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
moris遍历
二叉搜索树的中序遍历的值是递增的，但是遍历的时候到最左边无法返回，
这时给叶节点的右结点安排一个父节点。
首先对一个节点node，找到它左节点的的最右子节点，这个节点就是下一个比node大的节点
把这节点的right=node，然后再转到node的左节点，继续操作，直到叶节点，这个时候找到了最小的节点
赋值pre。然后找它的右节点，依次做以上操作。当一个节点重新进行以上操作时说明这个节点遍历过了
这个时候要找比它大的节点，就往右走。

总之，对于某个节点node 先找比他小的，如果没有就找比他大的
"""
class Solution(object):
    def recoverTree(self, root):
        x = None
        y = None
        pre = None
        tmp = None
        while root:
            if root.left:
                tmp = root.left
                while tmp.right and tmp.right!=root:
                    tmp = tmp.right
                if tmp.right is None:
                    tmp.right = root
                    root = root.left
                else:
                    if pre and pre.val>root.val:
                        y = root
                        if not x:
                            x = pre
                    pre = root
                    tmp.right = None
                    root = root.right
            else:
                if pre and pre.val>root.val:
                    y = root
                    if not x:
                        x = pre
                pre = root
                root = root.right
        if x and y:
            x.val,y.val = y.val,x.val



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


root = deserialize([1, 3, 'null', 'null', 2])
Solution().recoverTree(root)
print(root)