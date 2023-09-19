from typing import List

# tail[i]为长度为i的子序列，末尾的数字最小是多少
# tail[i]为递增的
# 对于nums中每个值，判断它在tail中应该排在哪个位置
# 则需要找第一个大于等于该值的位置
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail, res = [0] * len(nums), 0
        for num in nums:
            left, right = 0, res
            while left < right:
                mid = left + (right - left) // 2
                if tail[mid] > num:
                    right = mid
                elif tail[mid] == num:
                    right = mid
                else:
                    left = mid + 1
            tail[left] = num
            if left >= res:
                res += 1
        return res
