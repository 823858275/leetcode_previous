"""
第一步找到 数组中最后一个升序的情况 即nums[left]<nums[left+1] 这里left索引是需要大一点的数
然后第二步在left后面找到最后一个大于nums[left]的nums[right] 因为left后面的数是递减的
nums[right]是最小的大于nums[left]的数 最终将left后面的翻转（因为是递减的）
"""
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                left=i-1
                break
            if i==1:
                nums.reverse()
                return
        for i in range(len(nums)-1,left,-1):
            if nums[i]>nums[left]:
                right=i
                break
        nums[left],nums[right]=nums[right],nums[left]
        a=nums[left+1:]
        a.reverse()
        nums[left+1:]=a