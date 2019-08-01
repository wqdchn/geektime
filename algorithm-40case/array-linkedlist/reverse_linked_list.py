# @program: PyDemo
# @description: algorithm-40case/array & linkedlist
# https://leetcode.com/problems/reverse-linked-list
# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# @author: wqdong
# @create: 2019-08-01 10:53


#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    def reverseList2(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        if head.next == None:
            return head

        temp = head.next
        re_head = self.reverseList2(temp)
        head.next = None
        temp.next = head
        return re_head

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
head = s.reverseList(head)
while(head != None):
    print(head.val)
    head = head.next

# 2
head = s.createList()
head = s.reverseList(head)
while(head != None):
    print(head.val)
    head = head.next
