# @program: PyDemo
# @description: https://leetcode.com/problems/counting-bits/
# @author: wqdong
# @create: 2019-08-29 11:35
class Solution:
    def countBits(self, num: int):
        res = [0]
        for i in range(1, num + 1):
            res.append(bin(i).count("1")) # like leetcode 191 number of 1 bits
        return res

    def countBits2(self, num: int):
        res = [0]*(num+1)
        for i in range(1, num+1):
            res[i] += res[i & i-1] + 1
        return res[:num+1]

s = Solution()
num = 2
print(s.countBits(num))
num = 6
print(s.countBits(num))

num = 2
print(s.countBits2(num))
num = 6
print(s.countBits2(num))