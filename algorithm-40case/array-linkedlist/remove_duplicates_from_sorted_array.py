# @program: PyDemo
# @description: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# @author: wqdong
# @create: 2019-11-03 18:11

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0: return 0
        result = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[result] = nums[i]
                result += 1
        return result


s = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(s.removeDuplicates(nums))
