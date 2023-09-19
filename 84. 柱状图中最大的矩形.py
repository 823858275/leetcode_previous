# 单调栈(递增)
# 对于每个位置的heights[i]，矩形面积为到两边小于其高度为止的宽度
# 使用单调栈，如果栈顶height较大就弹出
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        stack = []
        stack.append(0)
        heights = [0] + heights + [0]
        size += 2
        area = 0
        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                area = max(area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        return area


print(Solution().largestRectangleArea([3, 4, 5, 6]))
