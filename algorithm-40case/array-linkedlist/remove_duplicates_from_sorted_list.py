# @program: PyDemo
# @description: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# @author: wqdong
# @create: 2020-01-20 11:15

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # Runtime: 36 ms, faster than 86.66% of Python3 online submissions for Remove Duplicates from Sorted List.
    def deleteDuplicates(self, head):
        dummy = ListNode("inf")
        dummy.next, prev = head, dummy
        while prev.next:
            if prev.next.val == prev.val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next

s = Solution()
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

head = s.deleteDuplicates(head)
while (head != None):
    print(head.val)
    head = head.next