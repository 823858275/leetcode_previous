class Solution:
    def FindKthToTail(self, head, k):
        if head == None or k == 0:
            return None
        fastNode = head
        slowNode = head
        for _ in range(k - 1):
            fastNode = fastNode.next
            if not fastNode:
                return None
        while fastNode.next:
            fastNode = fastNode.next
            slowNode = slowNode.next
        return slowNode
