#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#
# 二分查找，寻找峰值，分为序列是短递增，短递减的情况
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 判断特殊情况
        if not nums:
            return
        if len(nums) == 1:
            return 0
        # 二分查找
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:  # 如果是短递减的情况，则峰值肯定在左边
                r = mid
            else:  # 如果是短递增的情况，则峰值肯定在右边
                l = mid + 1
        return l
