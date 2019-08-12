# @program: PyDemo
# @description: https://leetcode.com/problems/sliding-window-maximum/
# @author: wqdong
# @create: 2019-08-12 13:23

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        if not nums: return []
        window , res = [], []
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= k -1:
                res.append(nums[window[0]])
        return res

s = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3

for i in s.maxSlidingWindow(nums, k):
    print(i)