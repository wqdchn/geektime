# @program: PyDemo
# @description: https://leetcode.com/problems/maximum-product-subarray/
# Example 1:
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# @author: wqdong
# @create: 2019-09-03 19:00


class Solution:

    # like dp
    def maxProduct(self, nums) -> int:
        if not nums:
            return 0
        imax = imin = res = nums[0]
        for num in nums[1:len(nums)]:
            imax, imin = max(num, imax * num, imin * num), min(num, imax * num, imin * num)
            res = max(res, imax)
        return res

    def maxProduct2(self, A):
        B = A[::-1] # list[<start>:<stop>:<step>] -1 mean reverses
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1  # if A[i-1] != 0: A[i] *= A[i-1] else: A[i] *= 1
            B[i] *= B[i - 1] or 1
        return max(A + B)

    # dp
    def maxProduct3(self, nums):
        if nums is None:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(2)]

        dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            x, y = i % 2, (i - 1) % 2
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            res = max(res, dp[x][0])

        return res


s = Solution()
nums = [2, 3, -2, 4]
print(s.maxProduct(nums))
print(s.maxProduct2(nums))

nums = [2, 3, -2, 4]
print(s.maxProduct3(nums))

