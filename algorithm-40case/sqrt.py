# @program: PyDemo
# @description: https://leetcode.com/problems/sqrtx/
# @author: wqdong
# @create: 2019-08-25 10:29


class Solution:
    def mySqrt(self, x: int) -> int:
        r = (x + 1) / 2
        while r * r > x:
            r = (r + x / r) // 2
        # return r
        return int(r)

    def mySqrt2(self, x):
        if x == 0 or x == 1:
            return x
        left, right = 0, x
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if mid == x / mid:
                return mid
            elif mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1
                res = mid
        return res


s = Solution()
print(s.mySqrt(5))
print(s.mySqrt2(5))

print(s.mySqrt(15))
print(s.mySqrt2(15))

print(s.mySqrt(1115))
print(s.mySqrt2(1115))