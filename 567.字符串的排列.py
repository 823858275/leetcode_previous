#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = [0] * 26
        dic2 = [0] * 26
        if len(s1) > len(s2):
            return False
        if len(s1) == 0:
            return False
        for i in range(len(s1)):
            dic1[ord(s1[i]) - 97] += 1
            dic2[ord(s2[i]) - 97] += 1
        if dic1 == dic2:
            return True
        for i in range(len(s1), len(s2)):
            dic2[ord(s2[i]) - 97] = dic2[ord(s2[i]) - 97] + 1
            dic2[ord(s2[i-len(s1)]) - 97] -= 1
            if dic1 == dic2:
                return True
        return False



