# @program: PyDemo
# @description: https://leetcode.com/problems/remove-element/
# @author: wqdong
# @create: 2019-11-04 19:17

class Solution:
    def removeElement(self, nums, val):
        if len(nums) == 0: return 0
        result = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[result] = nums[i]
                result += 1
        return result


s = Solution()

nums = [3, 2, 2, 3]
val = 3
print(s.removeElement(nums, val))
print(nums)

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(s.removeElement(nums, val))
print(nums)