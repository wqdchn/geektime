# @program: PyDemo
# @description: https://leetcode.com/problems/linked-list-cycle/
# @author: wqdong
# @create: 2019-08-06 14:12

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def createList(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = head.next.next
        # 1->2->3->4->5-> 指针回头指向3
        return head

s = Solution()

# 1
head = s.createList()
if s.hasCycle(head):
    print("链表有环！")
else:
    print("链表无环！")
