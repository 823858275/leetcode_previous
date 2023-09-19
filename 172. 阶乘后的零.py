"""
计算有多少0 相当于计算阶乘中出现了多少个2*5
对于n!=n * n-1 * n-2...*1 每隔两个数就会出现一个2 每隔5个就会出现一次5
2的个数肯定够用 关键看5出现的次数
对于n 会出现n/5次5 但是每25次会多出现一次5 每125次会多出现3次5...
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n // 5
            n = n // 5
        return count
