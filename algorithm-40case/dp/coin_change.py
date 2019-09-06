# @program: PyDemo
# @description: https://leetcode.com/problems/coin-change/
# @author: wqdong
# @create: 2019-09-06 09:32
class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1) # +1 表示需要走一步，也就是拿一个硬币

        return dp[-1] if dp[-1] != float('inf') else -1


s = Solution()
amount = 11
coins = [1, 2, 5]
print(s.coinChange(coins, amount))
