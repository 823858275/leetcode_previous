# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 在 head 到tail之间翻转链表 返回新的head tail
    def reverse(self, head, tail):
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        curNode = head
        while curNode != tail:
            nextNode = curNode.next
            curNode.next = pre
            pre = curNode
            curNode = nextNode
        return pre, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        tmpHead = head
        preNode = dummy
        curNode = head
        while curNode:
            for i in range(k):
                if curNode:
                    curNode = curNode.next
                else:
                    return dummy.next

            tmpHead, tail = self.reverse(tmpHead, curNode)
            preNode.next = tmpHead
            preNode=tail
            tail.next = curNode
            tmpHead = curNode
        return dummy.next


def genListNode(nums):
    dummy = ListNode()
    dummy.next = ListNode(nums[0])
    curNode = dummy.next
    for i in range(1, len(nums)):
        curNode.next = ListNode(nums[i])
        curNode = curNode.next
    return dummy.next


node=Solution().reverseKGroup(genListNode([1, 2, 3, 4, 5,6]), 2)
while node:
    print(node.val)
    node=node.next

