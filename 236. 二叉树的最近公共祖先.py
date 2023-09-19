class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果遍历到q或者p 或者空停止
        if root == p or root == q or not root:
            return root


        #在左边找p或者q
        left = self.lowestCommonAncestor(root.left, p, q)
        #在右边找p或者q
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果都没找到 返回空
        if not left and not right:
            return None
        # 如果只在一边找到 说明共同祖先是q或者p
        elif left and not right:
            return left
        elif not left and right:
            return right
        # 左右两边都有说明共同祖先是自身
        return root