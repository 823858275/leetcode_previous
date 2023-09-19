class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
使用中序遍历
在遍历过程中指定各个节点的前后节点
order_traversal 返回最左边的节点和最右边的节点 相当于头尾节点 然后把头尾节点相连
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return

        def order_traversal(node):

            if node.left:
                l_left, l_right = order_traversal(node.left)
                l_right.right = node
                node.left = l_right
            else:
                l_left = node

            if node.right:
                r_left, r_right = order_traversal(node.right)
                r_left.left = node
                node.right = r_left
            else:
                r_right = node
            return l_left, r_right

        the_left, the_right = order_traversal(root)
        the_left.left = the_right
        the_right.right = the_left
        return the_left