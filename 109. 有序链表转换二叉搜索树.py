# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
如果先找到链表中间位置的节点，然后分成两边遍历，时间复杂度较高
采用中序遍历，先遍历到最左边的节点，然后从头到尾遍历链表
"""
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def get_length(head):
            ind = 0
            while head:
                ind += 1
                head = head.next
            return ind

        def buildTree(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode()
            root.left = buildTree(left, mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = buildTree(mid + 1, right)
            return root

        length = get_length(head)
        return buildTree(0, length - 1)

def genListNode(nums):
    dummy = ListNode()
    dummy.next = ListNode(nums[0])
    curNode = dummy.next
    for i in range(1, len(nums)):
        curNode.next = ListNode(nums[i])
        curNode = curNode.next
    return dummy.next

print(Solution().sortedListToBST(genListNode([-10, -3, 0, 5, 9])))