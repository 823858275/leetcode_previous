class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def solution(root):
    def dfs(leftNode,rightNode):
        if leftNode==None and rightNode==None:
            return True
        elif leftNode!=None and rightNode!=None:
            if leftNode.val==rightNode.val:
                return dfs(leftNode.left,rightNode.right) and dfs(leftNode.right,rightNode.left)
            else:
                return False
        else:
            return False
    if not root:
        return True
    else:
        return dfs(root.left,root.right)
