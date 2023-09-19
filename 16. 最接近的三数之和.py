from typing import List

# 三指针
# 将数组排序，对于索引i，第二个指针指向i+1，第三个指针指向n-1，如果加起来小了就第二个指针后移，反之第三个指针前移
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        n = len(nums)
        for i in range(n):
            # 重复的数不用遍历
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                s=nums[i] + nums[left] + nums[right]
                # 等于target就是最优解
                if s == target:
                    return target
                res = res if abs(s - target) > abs(res-target) else s
                if s < target:
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    left += 1
                if s > target:
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    right -= 1
        return res


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
