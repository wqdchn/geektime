# @program: PyDemo
# @description: https://leetcode.com/problems/length-of-last-word/
# @author: wqdong
# @create: 2020-01-24 09:54

class Solution:

    # Runtime: 24 ms, faster than 84.99% of Python3 online submissions for Length of Last Word.
    def lengthOfLastWord(self, s):
        return 0 if (not s or s.isspace()) else len(s.split()[-1])

    # Runtime: 36 ms, faster than 8.87% of Python3 online submissions for Length of Last Word.
    def lengthOfLastWord2(self, s):
        lastlen = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " and lastlen > 0:
                return lastlen
            elif s[i] != " ":
                lastlen = lastlen + 1
        return lastlen


sl = Solution()
str = "Hello World"
print(sl.lengthOfLastWord(str))
print(sl.lengthOfLastWord2(str))


