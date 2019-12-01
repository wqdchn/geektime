# @program: PyDemo
# @description: https://leetcode.com/problems/implement-strstr/
# @author: wqdong
# @create: 2019-12-01 20:17

class Solution:
    def strStr(self, haystack: str, needle: str) -> int: # Runtime: 40 ms, faster than 49.67% of Python3 online submissions for Implement strStr().
        len_needle = len(needle)
        len_haystack = len(haystack)
        if len_needle == 0: return 0
        if len_needle > len_haystack: return -1
        for i in range(len_haystack):
            if haystack[i:i + len_needle] == needle:
                return i
        return -1


s = Solution()

needle = "ll"
haystack = "hello"

print(s.strStr(haystack, needle))
