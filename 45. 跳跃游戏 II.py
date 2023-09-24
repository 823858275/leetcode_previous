from typing import List

# 贪心，每次跳到最远的距离
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        max_pos = 0
        step = 0
        for i in range(len(nums) - 1):
            max_pos = max(max_pos, nums[i] + i)
            if i == end:
                end = max_pos
                step += 1
        return step
