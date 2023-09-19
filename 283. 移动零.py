from typing import List
#双指针 left用于存放非0元素的交换位置
#right用于寻找非0元素
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=right=0
        while right<len(nums):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
            right+=1

