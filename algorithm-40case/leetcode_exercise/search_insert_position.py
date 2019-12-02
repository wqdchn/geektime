# @program: PyDemo
# @description: https://leetcode.com/problems/search-insert-position/
# @author: wqdong
# @create: 2019-12-02 11:49

class Solution:
    # Runtime: 68 ms, faster than 7.61% of Python3 online submissions for Search Insert Position.
    def searchInsert(self, nums: [int], target: int) -> int:
        if target < nums[0]: return 0
        if target > nums[len(nums) - 1]: return len(nums)
        for i, v in enumerate(nums):
            if v == target: return i
        for i, v in enumerate(nums):
            if v > target: return i

    # Runtime: 36 ms, faster than 99.91% of Python3 online submissions for Search Insert Position.
    def searchInsert2(self, nums: [int], target: int) -> int:
        if target < nums[0]: return 0
        if target > nums[len(nums) - 1]: return len(nums)
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

    # Runtime: 64 ms, faster than 25.64% of Python3 online submissions for Search Insert Position.
    def searchInsert3(self, nums: [int], target: int) -> int:
        return len([x for x in nums if x < target])


s = Solution()
nums = [1, 3, 5, 6]
target = 2
print(s.searchInsert(nums, target))
print(s.searchInsert2(nums, target))
print(s.searchInsert3(nums, target))
