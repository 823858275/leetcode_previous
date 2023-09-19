from typing import List
# Fisher-Yates 洗牌算法
# 每次从i到数组末尾，随机取一个索引与i位置交换
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.origin = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.origin
        self.origin = list(self.array)
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
