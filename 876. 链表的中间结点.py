# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 快慢指针，快指针两步，慢指针一步
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slowNode=fastNode=head
        while fastNode and fastNode.next:
            slowNode=slowNode.next
            fastNode=fastNode.next.next
        return slowNode