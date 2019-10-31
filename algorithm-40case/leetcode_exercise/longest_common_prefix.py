# @program: PyDemo
# @description: https://leetcode.com/problems/longest-common-prefix/
# @author: wqdong
# @create: 2019-10-31 13:19
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        strs_min = min(strs, key=len)

        for i, v in enumerate(strs_min):
            for c in strs:
                if c[i] != v:
                    return strs_min[0:i]
        return strs_min


s = Solution()
strs = ["flower", "flow", "flight"]
print(s.longestCommonPrefix(strs))