"""
dp[i][j] 表示从nums中0-i的元素进行加减得到j的方案
dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
j的上限的设置 如果j上界设置为target 则上式会出现越界
所以设置为nums中所有元素都+ 或者-
"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > abs(total):
            return 0
        row, col = len(nums), 2 * total + 1
        dp = [[0] * col for _ in range(row)]
        if nums[0] == 0:
            dp[0][total] = 2
        else:
            dp[0][total + nums[0]] = 1
            dp[0][total - nums[0]] = 1
        for i in range(1, row):
            for j in range(col):
                left = j - nums[i] if j - nums[i] >= 0 else 0
                right = j + nums[i] if j + nums[i] < col else 0
                dp[i][j] = dp[i - 1][left] + dp[i - 1][right]
        return dp[row - 1][total + target]


"""
二维压缩成一维
用两个数组来保存
"""


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > abs(total):
            return 0
        row, col = len(nums), 2 * total + 1
        pre = [0] * col
        cur = [0] * col
        if nums[0] == 0:
            pre[total] = 2
        else:
            pre[total + nums[0]] = 1
            pre[total - nums[0]] = 1
        for i in range(1, row):
            for j in range(col):
                left = pre[j - nums[i]] if j >= nums[i] else 0
                right = pre[j + nums[i]] if j + nums[i] < col else 0
                cur[j] = left + right
            pre = cur.copy()  # 拷贝防止pre cur同时变化
        return pre[total + target]
