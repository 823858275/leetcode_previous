#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#快慢指针，寻找倒数第n+1个结点
#定义哑结点，处理链表只有一个结点的情况
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or n < 0:
            return None
        dummy = ListNode(0)
        dummy.next = head
        fastNode = dummy
        slowNode = dummy
        for _ in range(n + 1):
            fastNode = fastNode.next
        while fastNode:
            fastNode = fastNode.next
            slowNode = slowNode.next
        slowNode.next = slowNode.next.next
        return dummy.next
