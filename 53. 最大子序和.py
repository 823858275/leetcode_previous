from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = nums[0]
        lastsum = nums[0]
        for i in range(1, len(nums)):
            if cursum < 0:
                cursum = nums[i]
            else:
                cursum += nums[i]
            if cursum > lastsum:
                lastsum = cursum
        return lastsum
