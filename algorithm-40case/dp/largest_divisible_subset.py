# @program: PyDemo
# @description: https://leetcode.com/problems/largest-divisible-subset/
# @author: wqdong
# @create: 2019-09-10 14:42

class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums: return []
        nums.sort()
        n = len(nums)
        dp, index = [1] * n, [-1] * n
        max_dp, max_index = 1, 0
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    index[i] = j

            if max_dp < dp[i]:
                max_dp, max_index = dp[i], i

        res = []
        while max_index != -1:
            res.append(nums[max_index])
            max_index = index[max_index]
        return res

    def largestDivisibleSubset2(self, nums):
        dp = [[]]
        for n in sorted(nums):
            dp.append([n] + max((s for s in dp if not s or n % s[0] == 0), key=len))
        return max(dp, key=len)

    def largestDivisibleSubset3(self, nums):
        if not nums: return []
        nums.sort()
        d = {num: i for i, num in enumerate(nums)}
        dp = [[1, -1] for _ in nums]
        mxid = 0
        for i, num in enumerate(nums[1:], 1):
            for t in range(1, int(num ** .5) + 1):
                if num % t != 0: continue
                if t in d and dp[d[t]][0] + 1 > dp[i][0]:
                    dp[i] = dp[d[t]][0] + 1, d[t]
                t2 = num // t
                if t2 < num and t2 in d and dp[d[t2]][0] + 1 > dp[i][0]:
                    dp[i] = dp[d[t2]][0] + 1, d[t2]
            if dp[i][0] > dp[mxid][0]: mxid = i
        ans = []
        while mxid != -1:
            ans.insert(0, nums[mxid])
            mxid = dp[mxid][1]
        return ans


s = Solution()
nums = [1, 2, 3]
print(s.largestDivisibleSubset(nums))
print(s.largestDivisibleSubset2(nums))
print(s.largestDivisibleSubset3(nums))
