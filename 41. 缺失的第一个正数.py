# 置换
# 数组的长度为n，则缺失的第一个正数处于0-n+1范围内
# 对于每个x，若其在1-n之间则把它放于正确的位置
# 最终确定没有正确位置的数
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] <= n and nums[i] > 0 and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


print(Solution().firstMissingPositive([4,3,1,5,6,2]))
