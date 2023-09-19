"""
将数组中各数表示成二进制的形式 然后各位相加
如果某个数重复出现3次 则其%3之后为0
最后将各位相加的结果%3 则即为最终的结果
用counts[32]表示整个数组中 二进制各位的和 索引31是最高位
然后遍历整个数组 对每个数num 把每位加入到counts
最后再求res
"""
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % m
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)