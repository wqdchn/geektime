# @program: PyDemo
# @description: https://leetcode.com/problems/merge-two-sorted-lists/
# @author: wqdong
# @create: 2019-11-01 11:00

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 == None : return l2
        if l2 == None : return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def createList(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        # 1->2->3->4->5
        return head

s = Solution()

l1 = s.createList()
l2 = s.createList()

merge_l = s.mergeTwoLists(l1,l2)

while merge_l:
    print(merge_l.val)
    merge_l = merge_l.next