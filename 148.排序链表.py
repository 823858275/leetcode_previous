# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
归并排序 找到中间的节点
然后分为左右两部分 对左右两部分进行排序
然后合并
"""
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(-1)
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return dummy.next

    def findMid(self, head):
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow