# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyNode = ListNode()
        dummyNode.next = head
        tmp = dummyNode

        while tmp.next and tmp.next.next:
            node1 = tmp.next
            node2 = tmp.next.next
            tmp.next = node2
            node1.next = node2.next
            node2.next = node1
            tmp = node1
        return dummyNode.next