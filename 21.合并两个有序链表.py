#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res=ListNode(0)
        curNode=res
        if l1==None:
            return l2
        if l2==None:
            return l1
        while l1 and l2:
            if l1.val>l2.val:
                curNode.next=l2
                curNode=curNode.next
                l2=l2.next
            else:
                curNode.next=l1
                curNode=curNode.next
                l1=l1.next
        if l1:
            curNode.next=l1
        if l2:
            curNode.next=l2
        return res.next

