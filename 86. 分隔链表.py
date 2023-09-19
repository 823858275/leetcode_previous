class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 维护两个链表 大链表和小链表
# 大链表存放值较大的 小链表存放值较小的
# 最后小链表尾指向大链表头
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_dummy = ListNode()
        large_dummy = ListNode()
        small_cur = small_dummy
        large_cur = large_dummy
        cur_Node = head
        while cur_Node:
            if cur_Node.val >= x:
                large_cur.next = cur_Node
                large_cur = large_cur.next
                cur_Node = cur_Node.next
            else:
                small_cur.next = cur_Node
                small_cur = small_cur.next
                cur_Node = cur_Node.next
        small_cur.next = large_dummy.next
        large_cur.next = None
        return small_dummy.next