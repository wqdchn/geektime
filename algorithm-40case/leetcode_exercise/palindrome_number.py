# @program: PyDemo
# @description: https://leetcode.com/problems/palindrome-number/
# @author: wqdong
# @create: 2019-10-08 09:21

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        div = 1
        while x // div >= 10:
            div *= 10
        while x > 0:
            if x // div != x % 10: return False
            x = (x % div) // 10
            div /= 100
        return True


s = Solution()
x = 2147447412

if s.isPalindrome(x):
    print("is Palindrome number")
else:
    print("not Palindrome number")
