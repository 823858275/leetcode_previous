from typing import List

# 当矩形面积为0时肯定不存在重叠
# 求出矩形不重叠的情况，重叠就是不重叠的否
# 不重叠的情况分4种：rec1在rec2的左、上、右、下侧
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False
        return not (rec1[2] <= rec2[0] or rec2[2] <= rec1[0] or rec1[1] >= rec2[3] or rec1[3] <= rec2[1])
