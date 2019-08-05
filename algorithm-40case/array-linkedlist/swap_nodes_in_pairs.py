# @program: PyDemo
# @description: https://leetcode.com/problems/swap-nodes-in-pairs/submissions/
#Given a linked list, swap every two adjacent nodes and return its head.
#You may not modify the values in the list's nodes, only nodes itself may be changed.
#Example:
#
#Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# @author: wqdong
# @create: 2019-08-05 15:16


#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return  self.next

    def createList(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        return head

s = Solution()

# 1
head = s.createList()
head = s.swapPairs(head)
while(head != None):
    print(head.val)
    head = head.next
