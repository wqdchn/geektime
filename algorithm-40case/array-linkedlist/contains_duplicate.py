# @program: PyDemo
# @description: https://leetcode.com/problems/contains-duplicate/
# @author: wqdong
# @create: 2020-02-04 09:46

class Solution:

    # Runtime: 124 ms, faster than 84.28% of Python3 online submissions for Contains Duplicate.
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

    # Runtime: 124 ms, faster than 84.28% of Python3 online submissions for Contains Duplicate.
    def containsDuplicate2(self, nums):
        mp = {}
        for num in nums:
            if num not in mp:
                mp[num] = 1
            else:
                return True
        return False

    # Runtime: 132 ms, faster than 46.61% of Python3 online submissions for Contains Duplicate.
    def containsDuplicate3(self, nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


sl = Solution()
nums = [1, 2, 3, 1]

if sl.containsDuplicate(nums):
    print("true")
else:
    print("false")

if sl.containsDuplicate2(nums):
    print("true")
else:
    print("false")

if sl.containsDuplicate3(nums):
    print("true")
else:
    print("false")
