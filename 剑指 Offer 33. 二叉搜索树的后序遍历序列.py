from typing import List

"""
递归：后续遍历是左右根
递归dfs判断left到right是否符合二叉搜索树
先判断左边是否都是小于root 然后判断右边是否都是大于root
"""
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def dfs(left, right):
            if left >= right:
                return True
            root = postorder[right]
            for i in range(left, right + 1):
                if postorder[i] > root:
                    break
            m = i - 1
            for i in range(m + 1, right + 1):
                if postorder[i] < root:
                    return False
            return right == i and dfs(left, m) and dfs(m + 1, right - 1)

        return dfs(0, len(postorder) - 1)

"""
单调栈 后续遍历的倒序为根右左
如果碰到降序的地方说明遍历到了左节点 然后依次从栈中弹出找当前的root
"""
# class Solution:
#     def verifyPostorder(self, postorder: List[int]) -> bool:
#         stack, root = [], float('inf')
#         for i in range(len(postorder) - 1, -1, -1):
#             if postorder[i] > root:
#                 return False
#             while stack and postorder[i] < stack[-1]:
#                 root = stack.pop()
#             stack.append(postorder[i])
#         return True

print(Solution().verifyPostorder([1, 3, 2, 6, 5]))
