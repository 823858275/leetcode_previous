"""
将链表分为前半部分和后半部分
然后将后半部分反转
然后合并前半部分和后半部分
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        # 找到链表的中点
        slowNode = head
        fastNode = head
        while fastNode.next and fastNode.next.next:
            slowNode = slowNode.next
            fastNode = fastNode.next.next
        # 链表翻转
        midNode = slowNode
        preNode = midNode
        curNode = midNode.next
        while curNode:
            tmp = curNode.next
            curNode.next = preNode
            preNode = curNode
            curNode = tmp
        midNode.next = None
        # 两部分链表合并
        l1 = head
        l2 = preNode
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next
            l1.next = l2
            l2.next = l1_tmp
            l1 = l1_tmp
            l2 = l2_tmp
