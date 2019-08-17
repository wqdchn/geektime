# @program: PyDemo
# @description: https://leetcode.com/problems/majority-element/
# note that majority element more than ⌊ n/2 ⌋ times!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# @author: wqdong
# @create: 2019-08-17 10:07

import collections

class Solution:

    # Force
    def majorityElement(self, nums) -> int:
        maj_count = len(nums) // 2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > maj_count:
                return num

    # Map
    def majorityElement2(self, nums) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key = counts.get)

    # Sort
    def majorityElement3(self, nums) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    # Divide and Conquer
    def majorityElement4(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            if lo == hi:
                return nums[lo]

            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            if left == right:
                return left

            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)


s = Solution()
nums = [1,1,3,3,3,4,4,4,4,4,4]# note that majority element more than ⌊ n/2 ⌋ times!!!

print(s.majorityElement(nums))
print(s.majorityElement2(nums))
print(s.majorityElement3(nums))
print(s.majorityElement4(nums))