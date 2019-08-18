# @program: PyDemo
# @description: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# @author: wqdong
# @create: 2019-08-18 15:23


class Solution:

    # force  199 / 200 test cases passed, and get time limit exceeded.
    def maxProfit(self, prices) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit

    # one pass iteration
    def maxProfit2(self, prices):
        max_profit = 0
        if len(prices) < 2:
            return 0
        min_prices = prices[0]
        for price in prices:
            if price < min_prices:
                min_prices = price
            if price - min_prices > max_profit:
                max_profit = price - min_prices
        return max_profit

    # dp
    def maxProfit3(self, prices):
        if len(prices) < 2:
            return 0
        length, min_price = len(prices), prices[0]
        dp = [0] * length
        for i in range(1, length):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - min_price)
        return dp[length - 1]


s = Solution()
prices = [1,2]

print(s.maxProfit(prices))
print(s.maxProfit2(prices))
print(s.maxProfit3(prices))
