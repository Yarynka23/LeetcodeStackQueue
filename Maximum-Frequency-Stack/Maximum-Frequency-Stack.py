class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

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

class FreqStack:
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0
    
    def push(self, val: int) -> None:
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        if f > self.max_freq:
            self.max_freq = f
        if f not in self.group:
            self.group[f] = Stack()
        self.group[f].push(val)
    
    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if self.group[self.max_freq].is_empty():
            self.max_freq -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()