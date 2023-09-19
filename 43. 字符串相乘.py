class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        c = 0
        res = str()
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            s = (n1 + n2 + c) % 10
            c = (n1 + n2 + c) // 10
            res = str(s) + res
            i -= 1
            j -= 1
        return '1' + res if c == 1 else res

    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = ''
        if num1=='0' or num2=='0':
            return '0'
        for i in range(m - 1, -1, -1):
            carry = 0
            n1 = int(num1[i])
            tmp = ''
            for j in range(n - 1, -1, -1):
                n2 = int(num2[j])
                mul = (n1 * n2 + carry) % 10
                carry = (n1 * n2 + carry) // 10
                tmp = str(mul) + tmp
            tmp = str(carry) + tmp if carry != 0 else tmp
            res = self.addStrings(res, tmp + '0' * (m - i - 1))
        return str(res)


print(Solution().multiply("123", '456'))
