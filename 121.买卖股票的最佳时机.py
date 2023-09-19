#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
#思路一：dp[i]=max(dp[i-1],price[i]-minPrice)
#思路二：实际求的是后面的峰值-前面谷值
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        minPrice=prices[0]
        maxprofit=prices[1]-prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minPrice:
                minPrice=prices[i]
            else:
                if prices[i]-minPrice>maxprofit:
                    #实现dp表达式，if判断条件实现最值判断
                    maxprofit=prices[i]-minPrice
        if maxprofit<0:
            return 0
        return maxprofit

