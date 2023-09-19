from typing import List
# 使用双向队列deque存储nums的index
# deque为单调减队列，每次进入新的元素，弹出队列中较小值，则最后队列中的元素是较大元素的index
# 同时判断是否还在窗口中
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        for i in range(k):
            while deque and nums[i] >= nums[deque[-1]]:
                deque.pop()
            deque.append(i)
        res = [nums[deque[0]]]
        for i in range(k, len(nums)):
            while deque and nums[i] >= nums[deque[-1]]:
                deque.pop()
            deque.append(i)
            while deque[0] <= i - k:
                deque.popleft()
            res.append(nums[deque[0]])
        return res
