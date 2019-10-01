# @program: PyDemo
# @description: https://leetcode.com/problems/add-two-numbers/
# @author: wqdong
# @create: 2019-10-01 14:31

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        divmod_carry = 0
        res = curr = ListNode(0)
        while l1 or l2 or divmod_carry:
            if l1:
                divmod_carry += l1.val
                l1 = l1.next
            if l2:
                divmod_carry += l2.val
                l2 = l2.next
            divmod_carry, divmod_val = divmod(divmod_carry, 10)
            curr.next = curr = ListNode(divmod_val)
        return res.next


s = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

res = s.addTwoNumbers(l1, l2)
while res:
    print(res.val)
    res = res.next
