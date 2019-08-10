# @program: PyDemo
# @description: https://leetcode.com/problems/implement-queue-using-stacks/discuss/298445/13-lines-python
# @author: wqdong
# @create: 2019-08-10 13:55
class implement_queue_using_stacks2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.input:
            self.output.append(self.input.pop())

        p = self.output.pop()

        while self.output:
            self.input.append(self.output.pop())

        return p


    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.input:
            self.output.append(self.input.pop())

        p = self.output[-1]

        while self.output:
            self.input.append(self.output.pop())

        return p

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.input) == 0 and len(self.output) == 0

q = implement_queue_using_stacks2()
q.push(1)
q.push(2)

q.pop()

q.push(3)
q.push(4)

q.pop()

print(q.peek())