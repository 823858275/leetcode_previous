from typing import List
"""
数组中的多数元素是多于一半的
用cur来存储当前数 count来计数
如果num与cur相等 则count+1 否则-1
遍历到最后 cur肯定是多数元素
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cur = None
        for num in nums:
            if count == 0:
                cur = num
            count += 1 if num == cur else -1
        return cur