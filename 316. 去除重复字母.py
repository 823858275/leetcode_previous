#思路同402，stack为单调栈，里面的字典序单调不增
import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #单调栈，存放最终结果
        stack=[]
        #计算每个字母出现频次
        remind_counter=collections.Counter(s)
        for c in s:
            if c not in stack:
                while stack and c<stack[-1] and remind_counter[stack[-1]]>0:
                    stack.pop()
                stack.append(c)
            remind_counter[c]-=1
        return ''.join(stack)