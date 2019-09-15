# @program: PyDemo
# @description: https://leetcode.com/problems/reverse-integer/
# @author: wqdong
# @create: 2019-09-15 13:02

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            res = int(str(x)[::-1])
        else:
            res = int('-' + str(x)[:0:-1])
        return res if -2147483648 <= res <= 2147483647 else 0


s = Solution()
print(s.reverse(12345))
print(s.reverse(1234500))
print(s.reverse(1534236469))
