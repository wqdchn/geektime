# @program: PyDemo
# @description: https://leetcode.com/problems/roman-to-integer/
# Example 1:
#
# Input: "III"
# Output: 3
# Example 2:
#
# Input: "IV"
# Output: 4
# Example 3:
#
# Input: "IX"
# Output: 9
# Example 4:
#
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 5:
#
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# @author: wqdong
# @create: 2019-10-12 11:11

class Solution:
    def romanToInt(self, s):
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res, p = 0, 'I'
        for c in s[::-1]:
            res, p = res - map[c] if map[c] < map[p] else res + map[c], c
        return res

    def romanToInt2(self, s):
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = map.get(s[0])
        for i in range(1, len(s)):
            if map[s[i]] > map[s[i-1]]:
                res += map[s[i]] - 2 * map[s[i-1]]
            else:
                res += map[s[i]]
        return res

s = Solution()
str = "LVIII"
print(s.romanToInt(str))
print(s.romanToInt2(str))
str = "MCMXCIV"
print(s.romanToInt(str))
print(s.romanToInt2(str))