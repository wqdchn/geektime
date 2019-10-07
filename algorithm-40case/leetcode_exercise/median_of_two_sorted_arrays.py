# @program: PyDemo
# @description: https://leetcode.com/problems/median-of-two-sorted-arrays/
# @author: wqdong
# @create: 2019-10-07 12:38

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)
        totallen = len1 + len2
        cut1, cut2, cutL, cutR = 0, 0, 0, len1

        while cutL <= cutR:
            cut1 = (cutR - cutL) // 2 + cutL
            cut2 = totallen // 2 - cut1

            l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            r1 = float('inf') if cut1 == len1 else nums1[cut1]
            r2 = float('inf') if cut2 == len2 else nums2[cut2]

            if l1 > r2:
                cutR = cut1 - 1
            elif l2 > r1:
                cutL = cut1 + 1
            else:
                if totallen % 2 == 0:
                    l1 = l1 if l1 > l2 else l2
                    r1 = r1 if r1 < r2 else r2
                    return (l1 + r1) / 2
                else:
                    r1 = r1 if r1 < r2 else r2
                    return r1
        return -1


s = Solution()
nums1 = [3, 5, 8, 9]
nums2 = [1, 2, 7, 10, 11, 12]
print(s.findMedianSortedArrays(nums1, nums2))
