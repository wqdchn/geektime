# @program: PyDemo
# @description: https://leetcode.com/problems/permutations/
# @author: wqdong
# @create: 2019-08-22 19:23
from functools import reduce

class Solution:
    def permute(self, nums):
        if len(nums) <= 1: return [nums]
        result = []
        for i, num in enumerate(nums):
            n = nums[0:i] + nums[i+1:len(nums)]
            for y in self.permute(n):
                result.append([num] + y)
        return result

    def permute2(self, nums):
        return reduce(lambda P, n: [p[:i] + [n] + p[i:] for p in P for i in range(len(p) + 1)], nums, [[]])

    def permute3(self, nums):
        length = len(nums)
        if length <= 1:
            return [nums]
        elif length == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]

        items = list()
        for i in range(len(nums)):
            for n_sub in self.permute3(nums[0:i] + nums[i + 1:len(nums)]):
                items.append([nums[i]] + n_sub)
        return items


s = Solution()
nums = [1, 2, 3]
print(s.permute(nums))
print(s.permute2(nums))
print(s.permute3(nums))

