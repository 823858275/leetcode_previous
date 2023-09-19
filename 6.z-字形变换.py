class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""] * min(numRows, len(s))
        if len(rows) == 1:
            return s
        curRow = 0
        Godown = False
        for c in s:
            rows[curRow] += c
            if curRow == 0 or curRow == numRows - 1:
                Godown = not Godown
            curRow = curRow + 1 if Godown else curRow - 1
        res = ""
        for row in rows:
            res += row
        return res
