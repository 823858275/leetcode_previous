from typing import List
# 首先求出各位的累加和，并且算出每个数字的凭此，每个数字余3之后的模
# 如果s%3为1，要么去掉数组中一个数字%3之后=1，要么去除两个%3=2
# 如果以上都不成立，说明数组中没有%3=1的，也没有两个%3=2的，说明数组里只有一个%3=2的，则与数组整个%3=1相矛盾
# 所以肯定有一个种情况成立，s%3=2同理
# 再次从小到大重新遍历求出结果
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        cnt, modulo = [0] * 10, [0] * 3
        s = 0
        for digit in digits:
            cnt[digit] += 1
            modulo[digit % 3] += 1
            s += digit

        remove_mod, rest = 0, 0
        if s % 3 == 1:
            remove_mod, rest = (1, 1) if modulo[1] >= 1 else (2, 2)
        elif s % 3 == 2:
            remove_mod, rest = (2, 1) if modulo[2] >= 1 else (1, 2)

        ans = ""
        for i in range(0, 10):
            for j in range(cnt[i]):
                if rest > 0 and remove_mod == i % 3:
                    rest -= 1
                else:
                    ans += str(i)
        if len(ans) > 0 and ans[-1] == "0":
            ans = "0"
        return ans[::-1]
print(Solution().largestMultipleOfThree([1,1]))