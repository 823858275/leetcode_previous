# 快乐数，即使是很大的一个数比如13个9，一轮过后也就13*81，很快会比243小（3个9的平方）
# 因此最终的结果要么就是到1，要么就是一个环
# 通过链表的快慢指针思想，如果是环最终快慢指针是相等，如果是1，快指针直接到1
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            res = 0
            while num != 0:
                res += (num % 10) ** 2
                num //= 10
            return res

        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1
print(Solution().isHappy(19))