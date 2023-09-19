class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(nums):
    root = TreeNode(nums[0])
    for i in range(1, len(nums)):
        createSortedTreeNode(root, nums[i])
    return root


def createSortedTreeNode(root, num):
    if not root:
        root = TreeNode(num)
        return root
    else:
        if num <= root.val:
            root.left = createSortedTreeNode(root.left, num)
        else:
            root.right = createSortedTreeNode(root.right, num)
    return root

print(solution([3,1,4,6,2,7]))