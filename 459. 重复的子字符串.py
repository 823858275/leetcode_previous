class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        left = right = 0
        n = len(s)
        for i in range(1, n // 2 + 1):
            if s[i] == s[0]:
                right = i
                while right < n and s[left] == s[right]:
                    if right == n - 1:
                        return True
                    left += 1
                    right += 1
                left = 0
        return False


print(Solution().repeatedSubstringPattern("abab"))
