# @program: PyDemo
# @description: https://leetcode.com/problems/find-the-difference/
# @author: wqdong
# @create: 2019-09-30 10:58
import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
        for c in t:
            count[c] -= 1
            if count[c] < 0:
                return c
        return None


so = Solution()
s = "abcde"
t = "abscde"
print(so.findTheDifference(s, t))
