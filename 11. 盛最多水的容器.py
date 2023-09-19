from typing import List

"""
双指针 头尾各一个 然后短板往内缩
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 1:
            return -1
        i, j, area = 0, len(height) - 1, 0
        while i < j:
            h = min(height[i], height[j])
            area = max(area, h * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area
