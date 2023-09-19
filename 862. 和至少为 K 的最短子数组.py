from typing import List
import collections


# 构建前缀和pre,单调递增队列存储前缀和的索引
# 对于前缀和pre中每一个元素，由于要构建一个单调递增队列，如果比队尾元素小，则弹出
# 再把该元素索引加进去（由于如果前缀和数字中间某个元素比较大，它是不可能构成正确的被减项）
# 再从前到后遍历每个索引看是否满足题目条件，满足就从队列中删去（因为后面再用到的话不可能结果比它小）

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        pre = [0]
        for num in A:
            pre.append(pre[-1] + num)
        dq = collections.deque()
        res = len(A) + 1
        for i, pi in enumerate(pre):
            while dq and pi <= pre[dq[-1]]:
                dq.pop()
            while dq and pi - pre[dq[0]] >= K:
                res = min(res, i - dq.popleft())
            dq.append(i)
        return res if res < len(A) + 1 else -1