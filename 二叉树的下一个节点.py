class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

"""
三种情况：某个节点有右子树，则右子树的最左侧节点为下一个节点
如果没右子树，找到它的父节点，如果它是父节点的左节点，父节点就是下一个节点
如果它是父节点的右孩子，则不断找父节点，直到一个节点的父节点的左结点是该节点，这个节点的父节点就是下一个节点
"""
class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node
        elif pNode.next:
            node = pNode
            while node.next:
                if node.next.left == node:
                    return node.next
                node = node.next
        return None
