# @program: PyDemo
# @description: https://leetcode.com/problems/longest-increasing-subsequence/
# @author: wqdong
# @create: 2019-09-05 10:50

class Solution:
    def lengthOfLIS(self, nums) -> int: # O(N)
        if not nums: return 0
        res, dp = 1, [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])  # 注意缩进
        return res


s = Solution()
nums = [0]
print(s.lengthOfLIS(nums))
