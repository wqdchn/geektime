# @program: PyDemo
# @description: https://leetcode.com/problems/intersection-of-two-linked-lists/
# @author: wqdong
# @create: 2020-01-31 09:48

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # Runtime: 164 ms, faster than 75.79% of Python3 online submissions for Intersection of Two Linked Lists.
    def getIntersectionNode(self, headA, headB):
        if not headA and not headB: return None
        a, b = headA, headB
        while a is not b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return a


sl = Solution()

temp = ListNode(8)

a = ListNode(4)
a.next = ListNode(1)
a.next.next = temp
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)

b = ListNode(5)
b.next = ListNode(0)
b.next.next = ListNode(1)
b.next.next.next = temp
b.next.next.next.next = ListNode(4)
b.next.next.next.next.next = ListNode(5)

rs = sl.getIntersectionNode(a, b)
if rs:
    print(rs.val)
