# 给定两个稀疏向量，计算它们的点积（数量积）。
# 实现类
# SparseVector：SparseVector(nums)
# 以向量nums初始化对象。dotProduct(vec)计算此向量与vec的点积。
# 稀疏向量是指绝大多数分量为0的向量。你需要高效地存储这个向量，并计算两个稀疏向量的点积。
#
# 进阶：当其中只有一个向量是稀疏向量时，你该如何解决此问题？
#
#
# 示例
# 1：
# 输入：nums1 = [1, 0, 0, 2, 3], nums2 = [0, 3, 0, 4, 0]
# 输出：8
# 解释：v1 = SparseVector(nums1), v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 1 * 0 + 0 * 3 + 0 * 0 + 2 * 4 + 3 * 0 = 8
# 示例
# 2：
# 输入：nums1 = [0, 1, 0, 0, 0], nums2 = [0, 0, 0, 0, 2]
# 输出：0
# 解释：v1 = SparseVector(nums1), v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 0 * 0 + 1 * 0 + 0 * 0 + 0 * 0 + 0 * 2 = 0
# 示例
# 3：
# 输入：nums1 = [0, 1, 0, 0, 2, 0, 0], nums2 = [1, 0, 0, 0, 3, 0, 4]
# 输出：6
#
# 提示：
#
# n == nums1.length == nums2.length
# 1 <= n <= 10 ^ 5
# 0 <= nums1[i], nums2[i] <= 100
from typing import List
from collections import defaultdict
class SparseVector:
    def __init__(self, nums: List[int]):
        self.idx_num_dic = defaultdict(int)
        for i, num in enumerate(nums):
            self.idx_num_dic[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0

        if len(self.idx_num_dic) < len(vec.idx_num_dic):  # 遍历短的字典
            for idx, num in self.idx_num_dic.items():
                res += num * vec.idx_num_dic[idx]
        else:
            for idx, num in vec.idx_num_dic.items():
                res += num * self.idx_num_dic[idx]

        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
