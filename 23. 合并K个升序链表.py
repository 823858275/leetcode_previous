from typing import List
import heapq

# 方法1：首先将列表里的链表的首结点放入堆中
# 再依次取链表的下一个节点
# 方法2：将链表两两合并
# 采用分治递归
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        queue = []
        dummy = ListNode()
        p = dummy
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(queue, (lists[i].val, i))
        while queue:
            val, idx = heapq.heappop(queue)
            p.next = ListNode(val)
            p = p.next
            if lists[idx].next:
                heapq.heappush(queue, (lists[idx].next.val, idx))
                lists[idx] = lists[idx].next
        return dummy.next


def genListNode(nums):
    dummy = ListNode()
    dummy.next = ListNode(nums[0])
    curNode = dummy.next
    for i in range(1, len(nums)):
        curNode.next = ListNode(nums[i])
        curNode = curNode.next
    return dummy.next


listNodes = [[1, 4, 5], [1, 3, 4], [2, 6]]
for i in range(len(listNodes)):
    listNodes[i] = genListNode(listNodes[i])
print(Solution().mergeKLists(listNodes))
