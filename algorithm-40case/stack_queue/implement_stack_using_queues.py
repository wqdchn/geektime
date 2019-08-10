# @program: PyDemo
# @description: https://leetcode.com/problems/implement-stack-using-queues/
# @author: wqdong
# @create: 2019-08-10 14:49
class implement_stack_using_queues:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queue == []

s = implement_stack_using_queues()
s.push(1)
s.push(2)

s.pop()

s.push(3)
s.push(4)

s.pop()

print(s.pop())