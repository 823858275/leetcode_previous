class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
先计算出链表的长度
然后取余（考虑到k>length）
如果快慢指针 快指针先走k%length步 然后慢指针走
然后把慢指针后面的链表搬到前面
"""


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        fastNode = head
        slowNode = head
        if k % length == 0:
            return head
        for i in range(k % length):
            fastNode = fastNode.next
        while fastNode.next:
            slowNode = slowNode.next
            fastNode = fastNode.next
        newHead = slowNode.next
        fastNode.next = head
        slowNode.next = None
        return newHead