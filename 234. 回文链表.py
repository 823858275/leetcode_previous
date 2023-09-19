# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
首先通过快慢指针 找到链表的中点即慢指针位置
然后将链表的后半部分翻转 然后两端开始遍历判断是否相等
最后再将链表还原
"""
class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        fastNode = head
        slowNode = head
        while fastNode.next is not None and fastNode.next.next is not None:
            fastNode = fastNode.next.next
            slowNode = slowNode.next
        second_half_start = self.reverse_list(slowNode.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        slowNode.next = self.reverse_list(second_half_start)
        return result

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
