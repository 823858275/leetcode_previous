from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m, res = len(s), len(p), []
        if n < m:
            return res
        s_cnt = [0] * 26
        p_cnt = [0] * 26
        for i in range(m):
            p_cnt[ord(p[i]) - ord('a')] += 1
        left = 0
        for right in range(n):
            s_cnt[ord(s[right]) - ord('a')] += 1
            while s_cnt[ord(s[right]) - ord('a')] > p_cnt[ord(s[right]) - ord('a')]:
                s_cnt[ord(s[left]) - ord('a')] -= 1
                left += 1
            if right - left + 1 == m:
                res.append(left)
        return res
