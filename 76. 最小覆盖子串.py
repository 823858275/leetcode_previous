# 滑动窗口
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        match = 0
        start, minLen = 0, float("inf")
        window = {}
        count = {}
        for i in t:
            count[i] = count.get(i, 0) + 1
        while r < len(s):
            c = s[r]
            if count.get(c):
                window[c] = window.get(c, 0) + 1
                if window[c] == count[c]:
                    match += 1
            r += 1
            while match == len(count):
                if r - l < minLen:
                    minLen = r - l
                    start = l
                c = s[l]
                if count.get(c):
                    window[c] = window.get(c, 0) - 1
                    if window[c] < count[c]:
                        match -= 1
                l += 1
        return "" if minLen == float("inf") else s[start:start + minLen]
