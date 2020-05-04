"""
Queues

Should not be implemented with arrays, because unshifting for deletion is expensive
"""

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.first = Node()
        self.last = self.first
        self.length = 0

    def peek(self):
        if self.length == 0:
            return None
        return self.first.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return self
    
    def dequeue(self):
        if self.length == 0:
            return None
        if self.length == 1:  # if self.first == self.last
            self.last = None
        dequeued = self.first.value  # holding pointer if we need the dequeued value. else it will be removed by the garbage collector
        self.first = self.first.next
        self.length -= 1
        return dequeued


queue = Queue()
print(queue.peek())
queue.enqueue("John")
print(queue.peek())
queue.enqueue("Matt")
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(" ")
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())
print(queue.first)
print(queue.last)
