class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0
            tmp_sum = (x + y + carry) % 2
            carry = (x + y + carry) // 2
            res = str(tmp_sum) + res
            i-=1
            j-=1
        return res
