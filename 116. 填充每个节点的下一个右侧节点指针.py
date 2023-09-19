"""
利用节点的next指针
在某一行遍历的时候 相当于一个链表的遍历 然后设置下一行的next节点指向
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root