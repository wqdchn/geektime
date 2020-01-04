# @program: PyDemo
# @description: https://leetcode.com/problems/add-binary/
# @author: wqdong
# @create: 2020-01-04 10:32

class Solution:

    # Runtime: 48 ms, faster than 8.56% of Python3 online submissions for Add Binary.
    def addBinary(self, a, b):
        dif_lne = len(a) - len(b)
        if dif_lne > 0:
            b = "0" * dif_lne + b
        else:
            a = "0" * (-dif_lne) + a

        carry = 0
        sum = ""

        l = len(a) - 1

        while l >= 0:
            sum_temp = int(a[l]) + int(b[l]) + carry
            if sum_temp >= 2:
                carry = 1
                sum = str(sum_temp - 2) + "" + sum
            else:
                carry = 0
                sum = str(sum_temp) + "" + sum
            l -= 1
        if carry == 1:
            sum = "1" + sum;
        return sum

s = Solution()
a = "1010"
b = "10111"
print(s.addBinary(a, b))
