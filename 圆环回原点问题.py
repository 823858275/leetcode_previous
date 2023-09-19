# 圆环上有10个点，编号为0~9。从0点出发，每次可以逆时针和顺时针走一步，问走n步回到0点共有多少种走法。
# 输入: 2
# 输出: 2
# 解释：有2种方案。分别是0->1->0和0->9->0


# 本题考察的是动态规划。
# 如果你之前做过leetcode的70题爬楼梯，则应该比较容易理解：走n步到0的方案数=走n-1步到1的方案数+走n-1步到9的方案数。
# 因此，若设dp[i][j]为从0点出发走i步到j点的方案数，则递推式为：
# dp[i][j] = dp[i-1][(j-1+length)%length] + dp[i-1][(j+1)%length]
# ps:公式之所以取余是因为j-1或j+1可能会超过圆环0~9的范围









class Solution:
    def backToOrigin(self,n):
        #点的个数为10
        length = 10
        dp = [[0 for i in range(length)] for j in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for j in range(length):
                #dp[i][j]表示从0出发，走i步到j的方案数
                dp[i][j] = dp[i-1][(j-1+length)%length] + dp[i-1][(j+1)%length]
        return dp[n][0]