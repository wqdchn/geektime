# @program: PyDemo
# @description: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# @author: wqdong
# @create: 2019-08-18 13:20

class Solution:

    # force/greedy
    def maxProfit(self, prices) -> int:
        profit = 0
        for i in range(0, len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit

    # force/greedy
    def maxProfit2(self, prices) -> int:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

s = Solution()
prices = [7,1,5,3,6,4]

print(s.maxProfit(prices))
print(s.maxProfit2(prices))