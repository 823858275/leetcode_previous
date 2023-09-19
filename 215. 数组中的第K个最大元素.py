from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        while True:
            mid = self.partition(nums, left, right)
            if mid == len(nums) - k:
                return nums[mid]
            elif mid > len(nums) - k:
                right = mid - 1
            else:
                left = mid + 1

    def partition(self, nums, left, right):
        poivt = nums[left]
        start = left
        end = right
        while start < end:
            while start < end and nums[end] >= poivt:
                end -= 1
            nums[start] = nums[end]
            while start < end and nums[start] < poivt:
                start += 1
            nums[end] = nums[start]
        nums[start] = poivt
        return start


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
