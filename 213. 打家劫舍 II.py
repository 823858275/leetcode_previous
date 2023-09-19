"""
环形的屋子 类似于198的打家劫舍
首尾的房子只能偷一家 所以在nums中去掉首或者尾
然后求能获取的最大金额 选两者较大值
"""


class Solution:
    def rob(self, nums: [int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur

        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]
