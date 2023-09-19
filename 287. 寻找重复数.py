from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)-1
        for i in range(len(nums)):
            while nums[i]!=i+1:
                if nums[nums[i]-1]==nums[i]:
                    return nums[i]
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]