# @program: PyDemo
# @description: https://leetcode.com/problems/two-sum/
# @author: wqdong
# @create: 2019-08-14 11:05


class Solution:
    def twoSum(self, nums, target: int):
        mp = {}
        for i, x in enumerate(nums):
            if x in mp:
                return mp[x], i
            else:
                mp[target - x] = i
        return -1


s = Solution()
nums = [2, 7, 11, 15]
target = 9

print(s.twoSum(nums, target))