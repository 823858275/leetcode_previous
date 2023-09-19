# 前缀和+哈希表
# 用pre_sum表示0-i的和，哈希表存放pre_sum的个数
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = dict()
        count[0] = 1
        pre_sum = 0
        res = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            if count.get(pre_sum - k):
                res += count[pre_sum - k]
            count[pre_sum] = count.get(pre_sum, 0) + 1
        return res


print(Solution().subarraySum([1, -1, 0], 0))
