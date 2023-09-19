class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            counter[s[i]] = counter.get(s[i], 0) + 1
        for i in range(len(t)):
            if counter.get(t[i], 0) == 0:
                return False
            else:
                counter[t[i]] -= 1

        return True
