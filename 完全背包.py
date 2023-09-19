# 类似于01背包，题中的物体可以选择任意多个
# dp[i][j]=max(dp[i-1][j],dp[i][j-w[i]]+v[i])，对于第i个物品可以取多个，则分两种情况，1、不取该物品dp[i-1][j]
# 前i-1个物品装入背包容量为j的数组，2、至少取一件该物品，前i件物品装入背包容量为j-c[i]的数组（已经装了一件第i个物品）
# 表达式为dp[i][j-c[i]]+w[i]
# 优化上式：对于每一轮i，j从第c[i]个值开始递增，则dp[i][j]依赖于上一轮的后半段以前当前轮的前半段，当前轮的前半段又与
# 上一轮的前半段相等。（因为j<c[i]）
# 则表达式优化为dp[j]=max(dp[j],dp[j-w[i]]+v[i])
def FindMax(n, value, weight, capacity):
    dp = [0] * (capacity + 1)
    for i in range(1, n + 1):
        for j in range(1, capacity+1):
            if i == 1:
                if j < weight[i - 1]:
                    continue
                else:
                    dp[j] = j // weight[i - 1] * value[i - 1]
            else:
                if j < weight[i - 1]:
                    continue
                else:
                    dp[j] = max(dp[j], dp[j - weight[i - 1]] + value[i - 1])
    return dp[capacity]


N = 4
M = 6
w = [1, 2, 3, 4]
v = [1, 3, 4, 5]
print(FindMax(N, v, w, M))
