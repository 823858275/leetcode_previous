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


print(Solution().addStrings('9', '99'))
