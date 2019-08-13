# @program: PyDemo
# @description: https://leetcode.com/problems/valid-anagram/solution/
# @author: wqdong
# @create: 2019-08-13 12:12
import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return sorted(s) == sorted(t)

    def isAnagram2(self, s, t):
        if len(s) != len(t): return False
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2

    def isAnagram3(self, s, t):
        if len(s) != len(t): return False
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
        for c in t:
            count[c] -= 1
            if count[c] < 0:
                return False
        return True

s = Solution()
str_s = "abc"
str_t = "cba"

if s.isAnagram3(str_s, str_t):
    print("is Anagram!")
else:
    print("not Anagram!")