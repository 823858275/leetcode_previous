# 形成丑数相当于从1开始，依次乘2，3，5
# 关键要找到最小的数
# 设置3指针分别指向乘2的数、乘3的数、乘5的数，取最小加入结果
# 某个指针指向的数用完后指针加一，避免重复取
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = []
        res.append(1)
        p2 = p3 = p5 = 0
        for i in range(1, n):
            res.append(min(2 * res[p2], 3 * res[p3], 5 * res[p5]))
            if res[-1] == 2 * res[p2]:
                p2 += 1
            if res[-1] == 3 * res[p3]:
                p3 += 1
            if res[-1] == 5 * res[p5]:
                p5 += 1
        return res[-1]


print(Solution().nthUglyNumber(10))
