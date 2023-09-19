from typing import List


# 双指针i,j
# i用于指向1区间，j用于指向2区间
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            left_boundry = max(firstList[i][0], secondList[j][0])
            right_boundry = min(firstList[i][1], secondList[j][1])
            if left_boundry <= right_boundry:
                ans.append([left_boundry, right_boundry])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return ans
