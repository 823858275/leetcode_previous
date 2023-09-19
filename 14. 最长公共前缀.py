from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return ""
        for i in range(len(strs[0])):
            tmp = strs[0][i]
            for j in range(1, len(strs)):
                if i > len(strs[j]) - 1 or tmp != strs[j][i]:
                    return res
            res += tmp
        return res
