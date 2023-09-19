from typing import List

# 结果要去重，对数组进行排序，最终的结果都是单调递增的，某个位置不能重复
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(ind, path, sum_path):
            if sum_path == target:
                res.append(path)
                return
            if ind == len(candidates) and sum_path != target:
                return
            for i in range(ind + 1, len(candidates)):
                # 防止同样的结果再出现一次
                if i>ind+1 and candidates[i-1]==candidates[i]:
                    continue
                if sum_path + candidates[i] <= target:
                    dfs(i, path + [candidates[i]], sum_path + candidates[i])
        candidates.sort()
        dfs(-1, [], 0)
        return res


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
