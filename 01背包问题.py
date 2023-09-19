# 有n个物品，价值v[i],重量w[i]，背包容量c，求最大价值
# dp法一，使用二维矩阵存储变量dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])，i为物品的编号，j为容量
# 如果不取第i个物品dp[i-1][j]，取第i个物品dp[i-1][j-w[i]]+v[i]

def FindMax1(n, value, weight, capacity):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if i == 1:  # 判断初值情况
                if j < weight[i - 1]:  # 当第i个物体超重时的情况
                    dp[i][j] == 0
                else:
                    dp[i][j] = value[i - 1]
            else:
                if j < weight[i - 1]:  # 超重的情况
                    dp[i][j] = dp[i - 1][j]
                else:  # 不超重时的dp表达式
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + value[i - 1])
    print(dp)
    return dp[n][capacity]


# 优化存储空间，将原来二维矩阵变成一维矩阵；对于每一个i，矩阵在不停的变化
# 原来的矩阵dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])，对于不同的i，只跟i-1时的dp相关
# 即对于每一个i，只考虑i-1的情况，同时需要j需要从大到小遍历。
# dp[j]=max(dp[j],dp[j-w[i]]+v[i])（表达式中右边的式子是前一轮i的结果）
def FindMax2(n, value, weight, capacity):
    dp = [0] * (capacity + 1)          #初始化dp 长度为capcity-1
    if n == 0 or capacity == 0:
        return 0
    for i in range(1, n + 1):          #判断每一个i时的情况
        for j in range(capacity, -1, -1):
            if i == 1:                 #判读i为1时的情况，即只有一个物品
                if j < weight[i - 1]:  #超重时的情况
                    dp[j] = 0
                else:
                    dp[j] = value[i - 1]
            else:
                if j >= weight[i - 1]: #不超重时更新dp
                    dp[j] = max(dp[j], dp[j - weight[i - 1]] + value[i - 1])
    return dp[capacity]


n = 4
c = 5
w = [1, 2, 3, 4]
v = [2, 4, 4, 5]
print(FindMax2(n, v, w, c))
