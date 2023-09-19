#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        i=0
        j=0
        sLen=len(haystack)
        pLen=len(needle)
        next=self.get_next(needle)
        while i<sLen and j<pLen:
            if j==-1 or haystack[i]==needle[j]:
                i+=1
                j+=1
            else:
                j=next[j]
        if j==pLen:
            return i-j
        else:
            return -1

    def get_next(self,p):
        plen=len(p)
        next=[0]*plen
        next[0]=-1
        k=-1
        j=0
        while j<plen-1:
            if k==-1 or p[j]==p[k]:
                j+=1
                k+=1
                if p[j]!=p[k]:
                    next[j]=k
                else:
                    next[j]=next[k]
            else:
                k=next[k]
        return next
