#类似消消乐
#遍历每个字符串，如果与栈顶相同，则将栈顶弹出（消去），否则添加元素
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for ch in S:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
