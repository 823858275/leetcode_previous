#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
#两种处理方式
#法1：寻找到旋转点，即数组中最小值的点，然后判断target值在数组的哪个部分
#法2：在二分的过程中判断target在前半段还是后半段
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #判断特殊情况
        if not nums:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        #二分查找
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if target >= nums[0]:#判断target位置在前半段还是后半段
                if nums[mid] < nums[0]:
                    right = mid - 1
                else:
                    if nums[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
            else:
                if nums[mid] >= nums[0]:
                    left = mid + 1
                else:
                    if nums[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
        return -1
