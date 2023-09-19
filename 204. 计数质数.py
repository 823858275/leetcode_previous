"""
枚举
"""

# class Solution:
#     def countPrimes(self, n: int) -> int:
#         res = 0
#         for num in range(2, n):
#             res += self.isPrime(num)
#         return res
#
#     def isPrime(self, x):
#         for i in range(2, int(x ** 1 / 2)+1):
#             if x % i == 0:
#                 return False
#         return True

"""
埃氏筛
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True] * (n + 1)
        ans = 0
        for num in range(2, n):
            if is_prime[num]:
                ans += 1
                for k in range(num, n // num + 1):
                    is_prime[num * k] = False
        return ans


print(Solution().countPrimes(10))
