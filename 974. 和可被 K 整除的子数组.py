from typing import List

# 前缀和+哈希表
# 根据同余定理，哈希表中记录pre_sum/K的值
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        record = {0: 1}
        res = 0
        pre_sum = 0
        for num in A:
            pre_sum += num
            res += record.get(pre_sum % K, 0)
            record[pre_sum % K] = record.get(pre_sum % K, 0) + 1
        return res
