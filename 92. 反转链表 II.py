class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummyNode=ListNode()
        dummyNode.next=head
        tmpHead=dummyNode
        for i in range(m-1):
            if tmpHead and tmpHead.next:
                tmpHead=tmpHead.next
        preNode=tmpHead
        curNode=tmpHead.next
        for i in range(n-m+1):
            if curNode:
                tmp=curNode.next
                curNode.next=preNode
                preNode=curNode
                curNode=tmp
        if tmpHead.next:
            tmpHead.next.next=curNode
        if tmpHead:
            tmpHead.next=preNode
        return dummyNode.next

def genListNode(nums):
    dummy = ListNode()
    dummy.next = ListNode(nums[0])
    curNode = dummy.next
    for i in range(1, len(nums)):
        curNode.next = ListNode(nums[i])
        curNode = curNode.next
    return dummy.next


node=Solution().reverseBetween(genListNode([3,5]), 1,2)
while node:
    print(node.val)
    node=node.next
