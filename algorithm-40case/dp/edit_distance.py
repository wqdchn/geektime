# @program: PyDemo
# @description: https://leetcode.com/problems/edit-distance/
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# @author: wqdong
# @create: 2019-09-08 09:23

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1): dp[i][0] = i;
        for j in range(n + 1): dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1),
                               dp[i - 1][j] + 1,
                               dp[i][j - 1] + 1)
        return dp[m][n]


s = Solution()
word1 = "horse"
word2 = "ros"
print(s.minDistance(word1, word2))
