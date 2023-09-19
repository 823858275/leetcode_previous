from typing import List


# 假设从位置0处开始走，计算每次剩余的gasSpace，找到最小的，最小的下一个就作为起点
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasSpace = 0
        gasMin = float('inf')
        for i in range(len(gas)):
            gasSpace += gas[i] - cost[i]
            if gasSpace < gasMin:
                ind = i
                gasMin = gasSpace
        return (ind + 1) % len(gas) if gasSpace >= 0 else -1  # 取模防止索引为最后一个的情况


print(Solution().canCompleteCircuit([3, 1, 1], [1, 2, 2]))
