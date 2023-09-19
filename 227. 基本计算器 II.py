"""
一个数字栈 一个操作符栈
如果碰到左括号 直接加入到操作符栈
如果碰到右括号 则把所有操作符都计算了 直到遇到左括号
如果是数字 则计算出最终的数
如果是运算符 如果栈内优先级>=当前运算符 则全部计算掉 直到遇到左括号
"""
class Solution:
    def calculate(self, s: str) -> int:
        oper_pri = {'-': 1,
                    '+': 1,
                    '*': 2,
                    '/': 2,
                    # '%': 2,
                    # '^': 3
                    }
        s = s.replace(' ', '')
        s = s.replace('(-', '(0-')
        s = s.replace('(+', '(0+')
        num_stack = [0]
        oper_stack = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == '(':
                oper_stack.append(c)
            elif c == ')':
                while oper_stack:
                    if oper_stack[-1] != '(':
                        self.cal(num_stack, oper_stack)
                    else:
                        oper_stack.pop()
                        break
            else:
                if c.isdigit():
                    num = 0
                    for j in range(i, len(s)):
                        if not s[j].isdigit():
                            break
                        num = num * 10 + int(s[j])
                    if j == len(s) - 1:
                        i = j
                    else:
                        i = j - 1
                    num_stack.append(num)
                else:
                    while oper_stack and oper_stack[-1] != '(':
                        if oper_pri[oper_stack[-1]] >= oper_pri[c]:
                            self.cal(num_stack, oper_stack)
                        else:
                            break
                    oper_stack.append(c)
            i += 1
        while oper_stack:
            self.cal(num_stack, oper_stack)
        return num_stack[-1]

    def cal(self, nums, oper):
        if len(nums) < 2:
            return
        if not oper:
            return
        b, a = nums.pop(), nums.pop()
        op = oper.pop()
        if op == '+':
            ans = a + b
        elif op == '-':
            ans = a - b
        elif op == '*':
            ans = a * b
        elif op == '/':
            ans = a // b
        nums.append(ans)


print(Solution().calculate("1+1+1"))
