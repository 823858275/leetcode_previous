from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ind = 0
        for i in range(len(nums)):
            if nums[i] != nums[ind]:
                nums[ind + 1] = nums[i]
                ind += 1
        return ind + 1

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))