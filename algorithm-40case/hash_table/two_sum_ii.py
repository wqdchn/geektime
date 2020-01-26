# @program: PyDemo
# @description: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# @author: wqdong
# @create: 2020-01-26 15:33

class Solution:

    # Runtime: 168 ms, faster than 5.09% of Python3 online submissions for Two Sum II - Input array is sorted.
    def twoSum(self, numbers, target):
        mp = {}
        for i, x in enumerate(numbers):
            if x in mp:
                return mp[x], i + 1
            else:
                mp[target - x] = i + 1
        return -1

    # Runtime: 56 ms, faster than 97.11% of Python3 online submissions for Two Sum II - Input array is sorted.
    def twoSum2(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r = r - 1
            else:
                l = l + 1
            if l == r: return []
        return [l + 1, r + 1]


sl = Solution()
numbers = [2, 7, 11, 15]
target = 9

print(sl.twoSum(numbers, target))
print(sl.twoSum2(numbers, target))
