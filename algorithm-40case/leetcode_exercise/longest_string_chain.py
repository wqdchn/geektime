# @program: PyDemo
# @description: https://leetcode.com/problems/longest-string-chain/
# Example1:
#
# Input: ["a", "b", "ba", "bca", "bda", "bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a", "ba", "bda", "bdca".
#
# Note:
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.
#
# @author: wqdong
# @create: 2019-09-23 13:13

class Solution:
    def longestStrChain(self, words):
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[0:i] + w[i + 1:len(w)], 0) + 1 for i in range(len(w)))
        return max(dp.values())


s = Solution()
words = ["a", "b", "ba", "bca", "bda", "bdca"]
print(s.longestStrChain(words))
