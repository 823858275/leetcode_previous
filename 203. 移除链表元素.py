# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy=ListNode()
        preNode=dummy
        dummy.next=head
        curNode=head
        while curNode:
            if curNode.val==val:
                preNode.next=curNode.next
                curNode=preNode.next
            else:
                curNode=curNode.next
                preNode=preNode.next
        return dummy.next