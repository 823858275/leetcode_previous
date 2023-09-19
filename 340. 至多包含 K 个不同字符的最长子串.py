class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        freq = {}
        l, r = 0, 0
        max_len = 0
        count = 0
        while r < len(s):
            if freq.get(s[r], 0)==0:
                count += 1
            freq[s[r]] = freq.get(s[r], 0) + 1
            while count > k:
                if freq.get(s[l]) == 1:
                    count -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len

print(Solution().lengthOfLongestSubstringKDistinct("aa",1))
