# Definition for singly-linked list.
# 奇数链表、偶数链表分开构建再首尾相连
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd_head = head
        even_head = head.next
        odd_Node = odd_head
        even_Node = even_head

        while odd_Node.next and odd_Node.next.next:
            odd_Node.next = odd_Node.next.next
            odd_Node = odd_Node.next
            if even_Node.next and even_Node.next.next:
                even_Node.next=even_Node.next.next
                even_Node=even_Node.next
        odd_Node.next=even_head
        even_Node.next=None
        return odd_head

def genListNode(nums):
    dummy = ListNode()
    dummy.next = ListNode(nums[0])
    curNode = dummy.next
    for i in range(1, len(nums)):
        curNode.next = ListNode(nums[i])
        curNode = curNode.next
    return dummy.next

print(Solution().oddEvenList(genListNode([1,2,3,4,5])))