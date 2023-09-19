# 字典树（10叉树）
# 从1开始遍历，cur=1
# 先计算cur与cur+1之间有多少，（计算同一层节点之间间隔多少）
# 如果跨度过大，就cur*10找下一个字典序位置

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k = k - 1
        while k > 0:
            num = self.getNum(n, cur, cur + 1)
            if num <= k:
                k -= num
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur

    def getNum(self, n, first, last):
        num = 0
        while first <= n:
            num += min(n + 1, last) - first
            first *= 10
            last *= 10
        return num

print(Solution().getNum(1000,100,500))