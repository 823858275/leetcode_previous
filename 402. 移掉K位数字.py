# 单调栈，栈内元素单调不降
# 对于一个数字序列，去除一个数，使其最小，则需要找到第一个 ‘大小’ 这种情况
# 去除‘大’
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k and stack and int(digit) < int(stack[-1]):
                stack.pop()
                k -= 1
            stack.append(digit)
        stack = stack[:-k] if k > 0 else stack
        return ''.join(stack).lstrip('0') or '0'
