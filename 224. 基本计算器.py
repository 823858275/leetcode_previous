# 用栈来存储，遇到括号的时候把左右括号里的内容，计算出括号的内容后再放入栈内
# class Solution:
#     def calculate(self, s: str) -> int:
#         digit = 0
#         stack = []
#         for ch in s:
#             if ch.isdigit():
#                 digit = digit * 10 + int(ch)
#             else:
#                 if ch == '(':
#                     stack.append(ch)
#                 elif ch == ')':
#                     exp_list = [digit]
#                     while stack[-1] != '(':
#                         exp_list.append(stack.pop())
#                     stack.pop()
#                     exp_list.reverse()
#                     stack.append(self.cal(exp_list))
#                     digit = 0
#                 elif ch == ' ':
#                     if digit != 0:
#                         stack.append(digit)
#                         digit = 0
#                 else:
#                     if digit != 0:
#                         stack.append(digit)
#                         stack.append(ch)
#                         digit = 0
#                     else:
#                         stack.append(ch)
#         if digit!=0:
#             stack.append(digit)
#         return self.cal(stack)
#
#     def cal(self, exp_list):
#         oper = res = 0
#         for i in range(len(exp_list)):
#             if exp_list[i] == '+':
#                 oper = 1
#             elif exp_list[i] == '-':
#                 oper = 2
#             else:
#                 if oper == 0:
#                     res += exp_list[i]
#                 elif oper == 1:
#                     res += exp_list[i]
#                 else:
#                     res -= exp_list[i]
#         return res

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0
        sign = 1
        for ch in s:
            if ch.isdigit():
                operand = (operand * 10) + int(ch)
            elif ch == '+':
                res += sign * operand
                sign = 1
                operand = 0
            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ch == ')':
                res += sign * operand
                res *= stack.pop()  # stack pop 1, sign
                res += stack.pop()  # stack pop 2, operand
                operand = 0
        return res + sign * operand


print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
