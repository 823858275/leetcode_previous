# 整数n分成k份，1、每份不能为空，2、有空缺
# 将n个苹果放进k个碗，1、没空，2、有空
# 1、不能为空的情况 k<=n
# dp[n][k]=dp[n-1][k-1]+dp[n-k][k]
# 情况1，至少有一个盒子只有一个小球 dp[n-1][k] 将前n-1个小球放到k-1个盒子，第k个盒子放第n个小球
# 情况2，没有一个盒子只有一个小球的情况（所以的盒子至少2个球） 将k个小球放k个盒子里，将n-k个小球放到k个盒子里
def division(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][1] = 1
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - j][j]
    return dp[n][k]


# 2、可以为空的情况
# dp[n][k]=dp[n][k-1]+dp[n-k][k]
# 情况1，至少有一个盒子为空 dp[n][k-1]
# 情况2，所有的盒子都不为空 dp[n-k][k]
# k>n时，dp[n][k]=dp[n][k-1]
def division(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][1] = 1
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            if j > i:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - j][j]


# 整数n分成k份，1、每份不能为空，2、有空缺
# 将n个苹果放进k个碗，1、没空，2、有空
# 1、不能为空的情况 k<=n
# dp[n][k]=dp[n-1][k-1]+dp[n-k][k]
# 情况1，至少有一个盒子只有一个小球 dp[n-1][k] 将前n-1个小球放到k-1个盒子，第k个盒子放第n个小球
# 情况2，没有一个盒子只有一个小球的情况（所以的盒子至少2个球） 将k个小球放k个盒子里，将n-k个小球放到k个盒子里
def division(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][1] = 1
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - j][j]
    return dp[n][k]


# 2、可以为空的情况
# dp[n][k]=dp[n][k-1]+dp[n-k][k]
# 情况1，至少有一个盒子为空 dp[n][k-1]
# 情况2，所有的盒子都不为空 dp[n-k][k]
# k>n时，dp[n][k]=dp[n][k-1]
def division(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][1] = 1
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            if j > i:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - j][j]
    return dp[n][k]
