from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums:
            # 只有num是连续序列的第一个数才进入循环中
            if num - 1 not in nums_set:
                cur_num = num
                cur_len = 0
                while cur_num in nums_set:
                    cur_len += 1
                    cur_num += 1
                max_len = max(max_len, cur_len)
        return max_len
