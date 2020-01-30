# @program: PyDemo
# @description: https://leetcode.com/problems/single-number/
# @author: wqdong
# @create: 2020-01-30 10:00

class Solution:

    # Runtime: 92 ms, faster than 42.22% of Python3 online submissions for Single Number.
    def singleNumber(self, nums):
        mp = {}
        for i in nums:
            try:
                mp.pop(i)
            except:
                mp[i] = 1
        return mp.popitem()[0]

    # Runtime: 120 ms, faster than 14.89% of Python3 online submissions for Single Number.
    def singleNumber2(self, nums):
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        for k, v in mp.items():
            if v == 1:
                return k

    # Runtime: 148 ms, faster than 12.13% of Python3 online submissions for Single Number.
    def singleNumber3(self, nums):
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]

    # Runtime: 168 ms, faster than 10.87% of Python3 online submissions for Single Number.
    def singleNumber4(self, nums):
        total = 0
        mp = {}

        for num in nums:
            if num in mp:
                total -= num
            else:
                total += num

            mp[num] = True

        return total


sl = Solution()
nums = [4, 1, 2, 1, 2]
print(sl.singleNumber(nums))
print(sl.singleNumber2(nums))
print(sl.singleNumber3(nums))
print(sl.singleNumber4(nums))
