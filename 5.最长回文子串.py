#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
#中心扩散法，以每个元素为中心（or每两个元素为中心），不断扩大，判断是否为回文串
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        size = len(s)
        maxLength = 1               #保存最大的长度
        maxLengthString = s[0]      #保存最长的回文串
        for i in range(size):       #依次遍历
            odd_string, odd_length = self.center_spread(s, size, i, i)  #奇数长度回文串
            even_string, even_length = self.center_spread(s, size, i, i + 1)#偶数长度回文串
            if odd_length > maxLength or even_length > maxLength:#判读当前回文串是否是最长
                maxLength = max(odd_length, even_length)
                maxLengthString = odd_string if odd_length > even_length else even_string
        return maxLengthString

    def center_spread(self, s, size, left, right):#该函数判断以left，right为中心，最长回文串以及对应的长度
        #当left==right，得到的是一个奇数长度的回文串
        #当left==right-1,得到的是一个偶数长度的回文串
        l = left
        r = right
        while l >= 0 and r < size and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r], r - l - 1
#动态规划
#dp[l][r]以l为左指针，r为右指针的字符串（左闭右闭）是否为回文串
#l<=r，所以dp为上三角矩阵，同时r==l时，dp[l][r]==True
#状态转移方程：dp[l, r] = (s[l] == s[r] and (r - l <= 2 or dp[l + 1, r - 1]))
#先判读两边的字符串是否相等，然后判读去掉两边字符之后的字符串是否>=1，再判读之前的状态dp[l + 1, r - 1]
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size=len(s)
        if size<=1:
            return s
        dp=[[False]*size for _ in range(size)]  #初始化
        maxLength=1     #保存最后的结果
        res=s[0]
        for r in range(1,size):
            for l in range(r):
                if s[l]==s[r] and (r-l<=2 or dp[l+1][r-1]):#状态
                    dp[l][r]=True                          #转移方程
                    cur_len=r-l+1                          #判断
                    if cur_len>maxLength:                  #是否
                        maxLength=cur_len                  #需要更新
                        res=s[l:r+1]
        return res


