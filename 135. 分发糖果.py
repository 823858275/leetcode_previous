from typing import List
"""
https://leetcode-cn.com/problems/candy/solution/ctan-xin-suan-fa-yi-ci-bian-li-chao-ji-x-cvgb/
inc 表示递增序列的长度 相当于递增序列最后一个位置的糖果数
dec 表示递减序列的糖果数
pre 表示前一个糖果数 只在升序时用到
在递增序列中 从1开始糖果数依次增加 一直到inc
然后在递减序列中 糖果数也是依次增加 但是是相对增加 实际结果要倒序
然后到了inc==dec时，说明递增序列的最大糖果数不够大了 需要dec+1
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ret = 1
        inc, dec, pre = 1, 0, 1

        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                dec = 0
                pre = (1 if ratings[i] == ratings[i - 1] else pre + 1)
                ret += pre
                inc = pre
            else:
                dec += 1
                if dec == inc:
                    dec += 1
                ret += dec
                pre = 1

        return ret
