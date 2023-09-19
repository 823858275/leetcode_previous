# 常规思路将x变为字符串，看前一半是否跟后一半相同，但是会额外占用空间
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        num = 0
        while x > num:
            num = num * 10 + x % 10
            x //= 10
        return x == num or x == num // 10
print(Solution().isPalindrome(11))