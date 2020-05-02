"""
Implementing a queue using a stack, which in turn is implemented with an array
"""

class Stack:
    ''' 
    Implemented using a built-in Python array
    '''
    def __init__(self):
        self.list = []

    def peek(self):
        "Returns top item without removing it from the stack"
        if len(self.list) == 0:
            return None
        return self.list[len(self.list) - 1]

    def push(self, value):
        "Returns stack with added value at the top"
        self.list.append(value)  # grows to the right
        return self

    def pop(self):
        "Returns top item and removes it from the stack"
        if len(self.list) == 0:  # or if not self.top
            return None
        popped = self.list[len(self.list) - 1]  # required if we want to return popped
        self.list.pop()
        return popped

    def is_empty(self):
        "Returns true if stack is empty and false otherwise"
        if len(self.list) == 0:
            return True
        else:
            return False

class Queue:
    def __init__(self):
        self.stack = Stack()

    def is_empty(self):
        if len(self.stack.list) == 0:
            return True
        else:
            return False

    def peek(self):
        if len(self.stack.list) == 0:
            return None
        return self.stack.list[0]

    def enqueue(self, value):
        self.stack.list.append(value)
        return self
    
    def dequeue(self):
        if len(self.stack.list) == 0:
            return None
        dequeued = self.stack.list[0]  # holding pointer if we need the dequeued value. else it will be removed by the garbage collector
        del(self.stack.list[0])
        return dequeued


queue = Queue()
print(queue.is_empty())
print(queue.peek())
queue.enqueue("A")
print(queue.is_empty())
print(queue.peek())
queue.enqueue("B")
print(queue.peek())
print(" ")
print(queue.dequeue())
print(queue.is_empty())
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.is_empty())
print(queue.peek())
