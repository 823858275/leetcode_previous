from typing import List
# 前缀和+二分查找
# 前缀和为递增数组，随机取一个值0到pre[-1]
# 然后二分查找第一个大于该数的索引
import random


class Solution:

    def __init__(self, w: List[int]):
        self.pre = [w[0]]
        for i in range(1, len(w)):
            self.pre.append(self.pre[-1] + w[i])

    def pickIndex(self) -> int:
        rd = int(random.random() * self.pre[-1])
        left, right = 0, len(self.pre)
        while left < right:
            mid = left + (right - left) // 2
            if self.pre[mid] <= rd:
                left = mid + 1
            else:
                right = mid
        return right

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
