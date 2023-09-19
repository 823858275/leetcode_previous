# 二分查找，乘法表i，j的位置值为i*j
# 从0到i*j，进行二分遍历，对于mid，计算小于等于mid的cnt
# 找第一个cnt大于等于k的mid
# 计算cnt：每行进行遍历
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 0, m * n + 1
        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            start = mid // n
            cnt = start * n
            for i in range(start + 1, min(mid + 1, m + 1)):
                cnt += min(mid // i, n)
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        return right


print(Solution().findKthNumber(2, 3, 6))
