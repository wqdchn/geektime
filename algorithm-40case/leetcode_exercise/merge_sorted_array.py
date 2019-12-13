# @program: PyDemo
# @description: https://leetcode.com/problems/merge-sorted-array/
# @author: wqdong
# @create: 2019-12-13 20:17

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[0:n] = nums2[0:n]


s = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3
s.merge(nums1, m, nums2, n)

print(nums1)