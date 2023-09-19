from typing import List


# 用变量max_dis记录最远能跳到哪个位置
# 当遍历到数组中某个位置i时，判断i是否大于max_dis，判断能否跳跃到该位置
# 当max_dis大于等于数组长度时，表示能跳到数组末尾
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_dis = nums[0]
        for i, num in enumerate(nums):
            if i > max_dis:
                return False
            else:
                max_dis = max(max_dis, i + num)
            if max_dis >= len(nums)-1:
                return True
