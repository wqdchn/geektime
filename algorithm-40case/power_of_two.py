# @program: PyDemo
# @description: https://leetcode.com/problems/power-of-two/
# @author: wqdong
# @create: 2019-08-29 09:55
from math import log


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & n - 1)

    def isPowerOfTwo2(self, n):
        return False if n <= 0 else bin(n).count('1') == 1

    def isPowerOfTwo3(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1

    def isPowerOfTwo4(self, n: int) -> bool:
        return n > 0 and 2**round(log(n, 2)) == n


s = Solution()
n = 4

if s.isPowerOfTwo(n) and s.isPowerOfTwo2(n) and s.isPowerOfTwo3(n) and s.isPowerOfTwo4(n):
    print("is power of two!")
else:
    print("not power of two!")
