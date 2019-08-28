# @program: PyDemo
# @description: https://leetcode.com/problems/number-of-1-bits/
# Example 1:
#
# Input: 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
# Example 2:
#
# Input: 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
# Example 3:
#
# Input: 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
# @author: wqdong
# @create: 2019-08-28 10:10


class Solution(object):

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count("1")

    def hammingWeight2(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        mask = 1
        for i in range(32):
            if n & mask:
                res += 1
            mask = mask << 1
        return res

    def hammingWeight3(self, n):
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res


s = Solution()

print(s.hammingWeight(0b00000000000000000000000000001011))
print(s.hammingWeight2(0b00000000000000000000000000001011))
print(s.hammingWeight3(0b00000000000000000000000000001011))