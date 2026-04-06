class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node=Node(item)
        if self.head is None:
            self.head =new_node
        else:
            probe=self.head
            while probe.next:
                probe=probe.next
            probe.next=new_node

    def pop(self):
        if self.head is None:
            return
        val = self.head.val
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.val

class MyStack(Queue):

    def __init__(self):
        super().__init__()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.head=Node(x,self.head)

    def pop(self):
        """
        :rtype: int
        """
        return super().pop()

    def top(self):
        """
        :rtype: int
        """
        return super().peek()

    def empty(self):
        """
        :rtype: bool
        """
        return super().is_empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()