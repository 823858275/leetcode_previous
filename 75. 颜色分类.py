from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right, i = 0, len(nums) - 1, 0
        while i <= right:
            while i <= right and nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            i += 1
        return nums
print(Solution().sortColors([2]))