class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(nums, start, end):
            if start >= end:
                return
            mid = nums[start]
            low, high = start, end
            while low < high:
                while low < high and nums[high] >= mid:
                    high -= 1
                nums[low] = nums[high]
                while low < high and nums[low] < mid:
                    low += 1
                nums[high] = nums[low]
            nums[low] = mid
            quick_sort(nums, start, low - 1)
            quick_sort(nums, low + 1, end)
        quick_sort(nums,0,len(nums)-1)
        return nums