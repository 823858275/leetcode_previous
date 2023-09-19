# stack1是主栈，依次存储元素
# stack2是副栈，将stack1的元素反过来
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []  # 主栈
        self.stack2 = []  # 辅助栈

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2:
            element = self.stack2.pop()
            self.stack2.append(element)
            return element
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        element = self.stack2.pop()
        self.stack2.append(element)
        return element

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0

queue=MyQueue()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.pop())
queue.push(4)
print(queue.pop())