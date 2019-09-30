# @program: PyDemo
# @description: https://leetcode.com/problems/number-of-lines-to-write-string/
# @author: wqdong
# @create: 2019-09-30 16:41

class Solution(object):
    def numberOfLines(self, widths, S):
        lines, width = 1, 0
        for c in S:
            w = widths[ord(c) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w

        return lines, width

s = Solution()
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
print(s.numberOfLines(widths, S))