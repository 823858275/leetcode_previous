# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        p = head
        # 第一步，按照当前节点的下一个节点，创造新的节点与当前节点穿插
        while p:
            newNode = Node(p.val, next=p.next)
            p.next = newNode
            p = newNode.next
        # 第二步，设置随机节点
        p = head
        while p:
            if p.random:
                # 新节点随机节点的位置指向原节点的下一个（新节点）
                p.next.random = p.random.next
            p = p.next.next
        # 将链表拆开 快慢指针
        p = head
        dummy = Node(0)
        curNode = dummy
        while p:
            curNode.next = p.next
            p.next = p.next.next
            curNode = curNode.next
            p = p.next
        return dummy.next


# 哈希表 key为原节点，value为新节点
# 先按照next遍历一次
# 再指定random
# class Solution(object):
#     def copyRandomList(self, head):
#         if not head:
#             return None
#         # 创建一个哈希表，key是原节点，value是新节点
#         d = dict()
#         p = head
#         # 将原节点和新节点放入哈希表中
#         while p:
#             new_node = Node(p.val, None, None)
#             d[p] = new_node
#             p = p.next
#         p = head
#         # 遍历原链表，设置新节点的next和random
#         while p:
#             # p是原节点，d[p]是对应的新节点，p.next是原节点的下一个
#             # d[p.next]是原节点下一个对应的新节点
#             if p.next:
#                 d[p].next = d[p.next]
#             # p.random是原节点随机指向
#             # d[p.random]是原节点随机指向  对应的新节点
#             if p.random:
#                 d[p].random = d[p.random]
#             p = p.next
#         # 返回头结点，即原节点对应的value(新节点)
#         return d[head]
