# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        preNode=head
        curNode=head.next
        while curNode:
            if curNode.val!=preNode.val:
                preNode.next=curNode
                preNode=preNode.next
            curNode=curNode.next
        preNode.next=None
        return head