from typing import List


# 从左往右计算面积，从右往左计算面积
# 减去最大的矩形面积，减去所有方块面积
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         s1, s2 = 0, 0
#         max1, max2 = 0, 0
#         for i in range(len(height)):
#             max1 = max(height[i], max1)
#             s1 += max1
#             max2 = max(height[-i - 1], max2)
#             s2 += max2
#         return s1 + s2 - len(height) * max1 - sum(height)

# 动态规划
class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        res=0
        for i in range(1,len(height)):
            max_left[i]=max(max_left[i-1],height[i-1])
            max_right[-i-1]=max(max_right[-i],height[-i])
        for i in range(1,len(height)-1):
            if height[i]<min(max_right[i],max_left[i]):
                res+=min(max_right[i],max_left[i])-height[i]
        return res

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
