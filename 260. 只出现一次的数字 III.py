from typing import List

# 异或具有交换率，两个相同的数异或之后为0，任何数异或0等于其自身
# 将数组中的元素从同到尾异或，最后的结果为只出现一次的两个数的异或结果
# 再根据异或的结果按照某个为1的位数将数组分成两部分
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for num in nums:
            res ^= num
        pos = 1
        while pos & res == 0:
            pos <<= 1
        num1, num2 = 0, 0
        for num in nums:
            if num & pos:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]
