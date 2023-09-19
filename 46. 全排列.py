from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, used, depth, size, path):
            if depth == size:
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, used, depth + 1, size, path)
                    used[i]=False
                    path.pop()

        dfs(nums, [False] * len(nums), 0, len(nums), [])
        return res
print(Solution().permute([1,2,3]))