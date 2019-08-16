# @program: PyDemo
# @description: https://leetcode.com/problems/powx-n/
# @author: wqdong
# @create: 2019-08-16 19:17

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow

    def myPow2(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow2(x, -n)
        if n % 2:
            return x * self.myPow2(x, n-1)
        return self.myPow2(x*x, n/2)

s = Solution()

print(s.myPow(2.00000, 10))
print(s.myPow2(2.00000, -2))
print(s.myPow(34.00515, -3))