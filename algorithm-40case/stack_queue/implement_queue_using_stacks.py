# @program: PyDemo
# @description: https://leetcode.com/problems/implement-queue-using-stacks/discuss/298445/13-lines-python
# @author: wqdong
# @create: 2019-08-10 13:25
class implement_queue_using_stacks:

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
        if len(self.input) == 0:
            while len(self.output) != 0:
                self.input.append(self.output.pop())

        self.input.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.output) == 0:
            while len(self.input) != 0:
                self.output.append(self.input.pop())

        return self.output.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.output) == 0:
            while len(self.input):
                self.output.append(self.input.pop())

        return self.output[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.input) == 0 and len(self.output) == 0

q = implement_queue_using_stacks()
q.push(1)
q.push(2)

q.pop()

q.push(3)
q.push(4)

q.pop()

print(q.peek())