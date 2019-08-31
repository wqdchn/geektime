# @program: PyDemo
# @description: https://leetcode.com/problems/climbing-stairs/
# @author: wqdong
# @create: 2019-08-31 10:39
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2: return n
        x, y = 1, 1
        for _ in range(1, n):
            x, y = y, x + y
        return y

    def climbStairs2(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2: return n
        res = [0] * n
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]
        return res[n - 1]

    def climbStairs3(self, n: int) -> int:
        def clim_bStairs3(i, n):
            if i > n: return 0
            if i == n: return 1
            return clim_bStairs3(i + 1, n) + clim_bStairs3(i + 2, n)
        return clim_bStairs3(0, n)


s = Solution()
print(s.climbStairs(35))
print(s.climbStairs2(35))
print(s.climbStairs3(35))# Time Limit Exceeded in leetcode
