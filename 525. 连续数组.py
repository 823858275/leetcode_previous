"""
前缀和+哈希表
cnt用于计数初始的时候是0 碰到0 就-1 碰到1 就+1
哈希表 key为cnt 对应的value是索引
当遍历数组的时候更新cnt 当遇到cnt出现在哈希表中的key时 相当于两个索引之间的0和1的个数相同
则结果为两个索引的差值
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0: -1}
        cnt, res = 0, 0
        for i in range(len(nums)):
            cnt = cnt + 1 if nums[i] == 1 else cnt - 1
            if cnt in dic:
                res = max(res, i - dic[cnt])
            else:
                dic[cnt] = i
        return res


print(Solution().findMaxLength([0, 0, 1]))