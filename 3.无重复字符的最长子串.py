#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# 滑动窗口，双指针，建立一个哈希表，key为字符，value为对应的索引
# 不停移动右指针，当哈希表中存在重复元素，移动左指针
#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left, right = 0, 0
        dic = {}
        max_length = float("-inf")
        while left < len(s) and right < len(s):
            if dic.get(s[right]) is not None:
                max_length = max(max_length, right - left)
                left = max(dic[s[right]] + 1, left)
                dic[s[right]] = right
            else:
                dic[s[right]] = right
            right += 1
        max_length = max(max_length, right - left)
        return max_length


print(Solution().lengthOfLongestSubstring("abba"))
