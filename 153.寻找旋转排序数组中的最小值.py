#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
# 二分查找
# 第一个数字肯定比第二部分增序数组中的每一个值都大
# 每次遍历跟第一个数字进行比较
# left始终在左半部分，right始终在右半部分
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 判断特殊情况
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        # 数组没有旋转
        if nums[r] > nums[l]:
            return nums[l]
        # 二分查找
        while r > l:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1
