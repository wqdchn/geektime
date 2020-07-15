# @program: geektime
# @description: https://leetcode.com/problems/n-th-tribonacci-number/
# @author: wqdong
# @create: 2020-07-15 20:07

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        return self.help(n)[2]

    def help(self, n):
        if n < 3:
            return (0, 1, 1)
        else:
            a, b, c = self.help(n - 1)
            return (b, c, a + b + c)

s = Solution()

print(s.tribonacci(25))