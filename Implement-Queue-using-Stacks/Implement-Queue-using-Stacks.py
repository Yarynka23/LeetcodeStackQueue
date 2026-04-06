class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# head = 1 -> 2 -> 3 -> 4
# head = 4 -> 3 -> 2 -> 1

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, next=self.head)

    def pop(self):
        if self.head is None:
            return None
        val = self.head.val
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.val

class MyQueue(Stack):
    def __init__(self):
        self.head=None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.head:
            self.head=Node(x)
        else:
            a=self.head
            while a.next:
                a=a.next
            a.next=Node(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.is_empty():
            return None
        return super().pop()

    def peek(self):
        """
        :rtype: int
        """
        return super().peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.head is None


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()