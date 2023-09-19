from typing import List


# 单调栈 栈内保存T的index，并且对应的温度越来越小
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res


print((Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])))
