# @program: PyDemo
# @description: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.
#
# Example:
#
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
# Note:
# You may assume that nums' length ≥ k-1 and k ≥ 1.
# @author: wqdong
# @create: 2019-08-11 11:15

import heapq

class kth_largest_element_in_a_stream:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """

        self.arr = nums
        self.k = k
        heapq.heapify(self.arr)
        while len(self.arr) > k:
            heapq.heappop(self.arr)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        if len(self.arr) < self.k:
            heapq.heappush(self.arr, val)
        elif val > self.arr[0]:
            heapq.heapreplace(self.arr, val)
        return self.arr[0]

k = 3
arr = [4,5,8,2]
kth = kth_largest_element_in_a_stream(k, arr)

print(kth.add(3))
print(kth.add(5))
print(kth.add(10))
print(kth.add(9))
print(kth.add(4))