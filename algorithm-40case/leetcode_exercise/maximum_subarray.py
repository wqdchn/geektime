# @program: PyDemo
# @description: https://leetcode.com/problems/maximum-subarray/
# @author: wqdong
# @create: 2019-12-30 12:25

class Solution:

    # Runtime: 72 ms, faster than 62.94% of Python3 online submissions for Maximum Subarray.
    def maxSubArray(self, nums):
        dp = [0] * (len(nums))
        max_sum = dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_sum = max(max_sum, dp[i])
        return max_sum

    # Runtime: 72 ms, faster than 62.94% of Python3 online submissions for Maximum Subarray.
    def maxSubArray2(self, nums):
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum


s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(nums))
print(s.maxSubArray2(nums))