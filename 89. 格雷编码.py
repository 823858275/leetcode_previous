from typing import List


# 设G[n]为n位格雷码的集合
# 则n+1位格雷码集合为 G[n]+将G[n]倒序，并且在前面加1（相当于+2的n次方）
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        head = 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        return res
