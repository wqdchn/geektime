# @program: PyDemo
# @description: https://leetcode.com/problems/plus-one/
# @author: wqdong
# @create: 2019-12-26 10:28

class Solution:

    # Runtime: 28 ms, faster than 90.22% of Python3 online submissions for Plus One.
    def plusOne(self, digits):
        for i in range(len(digits)):
            if(digits[~i] < 9):
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)

s = Solution()
digits = [1,3,9]
print(s.plusOne(digits))
