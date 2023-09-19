from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return None
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return -1
