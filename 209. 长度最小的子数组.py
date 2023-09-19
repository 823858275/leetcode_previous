from typing import List


# 前缀和+二分查找
# class Solution:
#     def minSubArrayLen(self, s: int, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         n = len(nums)
#         res = n
#         sums = [0]
#         for i in range(1, n + 1):
#             sums.append(sums[i - 1] + nums[i - 1])
#         for i in range(n):
#             left, right = i, n
#             while left < right:
#                 mid = (left + right) // 2
#                 target = s + sums[i]
#                 if sums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid
#             if sums[right] >= target:
#                 res = min(res, right - i)
#         return res if sums[-1]>=s else 0

# 双指针 滑动窗口 start end
# 移动end直到sum>=target 记录min_len
# 然后移动start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        start, end = 0, 0
        res = len(nums) + 1
        total = 0
        while end < len(nums):
            total += nums[end]
            if total >= s:
                res = min(res, end - start + 1)
                while start <= end:
                    total -= nums[start]
                    start += 1
                    if total >= s:
                        res = min(res, end - start + 1)
                    else:
                        break
            end += 1
        return 0 if res == (len(nums) + 1) else res


print(Solution().minSubArrayLen(4, [1,4,4]))
