from typing import List
# i从0到k，nums1取i个，nums2取k-i个
# 对于nums1或者nums2 求其取k个数时得到的最大数（单调栈）
# 再合并

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def findMaxK(nums, k):
            drop = len(nums) - k
            stack = []
            for num in nums:
                while stack and drop and num > stack[-1]:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            stack = stack[:k]
            return stack

        def merge(A, B):
            ans = []
            while A or B:
                bigger = A if A > B else B
                ans.append(bigger[0])
                bigger.pop(0)
            return ans

        return max(merge(findMaxK(nums1, i), findMaxK(nums2, k - i)) for i in range(k + 1) if
                   i <= len(nums1) and k - i <= len(nums2))


print(Solution().maxNumber([7, 3, 8, 0, 6, 5, 7, 6, 2], [2, 5, 6, 4, 4, 0], 15))
