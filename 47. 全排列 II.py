from typing import List


# 由于不能出现重复的，需要对数组先进行排序
# dfs中遍历时，要去除掉出现过的情况
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(depth, path, used):
            if depth == len(nums):
                res.append(path)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                if not used[i]:
                    used[i] = True
                    dfs(depth + 1, path + [nums[i]], used)
                    used[i] = False

        if not nums:
            return []
        nums.sort()
        used = [False] * len(nums)
        dfs(0, [], used)
        return res
