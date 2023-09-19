from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, max_multi, min_multi = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            max_tmp, min_tmp = max_multi, min_multi
            max_multi = max(nums[i], nums[i] * max_tmp, nums[i] * min_tmp)
            min_multi = min(nums[i], nums[i] * max_tmp, nums[i] * min_tmp)
            res = max(max_multi, res)
        return res
