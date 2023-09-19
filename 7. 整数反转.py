class Solution:
    def reverse(self, x: int) -> int:
        y, res = abs(x), 0
        boundry = (1 << 31) - 1 if x > 0 else 1 << 31
        while y > 0:
            res = y % 10 + res * 10
            if res > boundry:
                res = 0
            y //= 10
        return res if x > 0 else -res
