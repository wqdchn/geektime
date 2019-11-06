# @program: PyDemo
# @description: https://leetcode.com/problems/remove-linked-list-elements/
# @author: wqdong
# @create: 2019-11-06 21:09

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements1(self, head, val):
        dummy = ListNode(-1)
        dummy.next, prev = head, dummy
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next

    def removeElements2(self, head, val):
        if head == None: return None
        temp = self.removeElements2(head.next, val)
        if head.val == val: return temp
        head.next = temp
        return head

    def createList(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        return head


s = Solution()
head = s.createList()
head = s.removeElements1(head, 3)
while (head != None):
    print(head.val)
    head = head.next

head = s.createList()
head = s.removeElements2(head, 3)
while (head != None):
    print(head.val)
    head = head.next
