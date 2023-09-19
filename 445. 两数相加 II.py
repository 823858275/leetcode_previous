# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 用栈保存l1，l2的值

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        res = None
        carry = 0
        while stack1 or stack2 or carry:
            a = stack1.pop() if stack1 else 0
            b = stack2.pop() if stack2 else 0
            s = (a + b + carry) % 10
            carry = (a + b + carry) // 10
            curNode = ListNode(s)
            curNode.next = res
            res = curNode
        return res
