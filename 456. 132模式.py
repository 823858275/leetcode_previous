from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        left_min=[]
        left_min.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i]<left_min[-1]:
                left_min.append(nums[i])
            else:
                left_min.append(left_min[-1])

        right_min=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            cur=nums[i]
            if cur>left_min[i]:
                if cur<right_min:
                   right_min=cur
                elif cur>right_min and left_min[i]<right_min:
                    return True
            else:
                if cur<right_min:
                   right_min=cur
        return False

print(Solution().find132pattern([3,5,0,3,4]))