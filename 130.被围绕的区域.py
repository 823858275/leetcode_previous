#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        row=len(board)
        col=len(board[0])
        for j in range(col):
            if board[0][j]=="O":
                self.dfs(board,0,j)
        for j in range(col):
            if board[row-1][j]=="O":
                self.dfs(board,row-1,j)
        for i in range(row):
            if board[i][0]=="O":
                self.dfs(board,i,0)
        for i in range(row):
            if board[i][col-1]=="O":
                self.dfs(board,i,col-1)
        for i in range(0,row):
            for j in range(0,col):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="#":
                    board[i][j]="O"
    def dfs(self,board,i,j):
        board[i][j]="#"
        for k,v in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if self.isValid(board,k,v):
                self.dfs(board,k,v)
    def isValid(self,board,i,j):
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!="O":
            return False
        else:
            return True


        

