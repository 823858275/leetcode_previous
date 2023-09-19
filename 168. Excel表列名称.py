class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            res = res + chr((columnNumber % 26 + ord("A") - 1))
            columnNumber //= 26
        return res


print(Solution().convertToTitle(28))
