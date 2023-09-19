# 异或具有结合律
# 每个数与当前索引异或 然后跟最终结果异或 相当于把所有的数和其索引异或
# 最终剩下的就是丢失的数字
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= (i + 1) ^ nums[i]
        return res
