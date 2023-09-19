#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#
class Solution:
    def isValidSudoku(self, board):
        dic = {}
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == ".":
                    continue
                if dic.get(board[i][j]) != None:
                    for m in range(row):
                        if board[m][j] == board[i][j] and m != i:
                            return False
                    for n in range(col):
                        if board[i][n] == board[i][j] and n != j:
                            return False
                    for m in range(3):
                        for n in range(3):
                            if board[i // 3 * 3 + m][j // 3 * 3 + n] == board[i][j] and (i // 3 * 3 + m) != i and (j // 3 * 3 + n) != j:
                                return False
                dic[board[i][j]] = dic.get(board[i][j], 0) + 1
        return True
