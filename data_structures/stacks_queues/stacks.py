"""
Stacks

Can be implemented with arrays or linked lists
"""

class Stack:
    '''
    Implemented using arrays
    '''
    def __init__(self):  # could allow for empty initialisation instead
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

    def traverse(self):
        return self.list
    

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
"""
class Stack:
    '''
    Implemented using Linked Lists
    '''
    def __init__(self):  # could allow for empty initialisation instead
        self.bottom = Node()
        self.top = self.bottom
        self.length = 0

    def peek(self):
        "Returns top item without removing it from the stack"
        return self.top

    def push(self, value):
        "Returns stack with added value at the top"
        new_node = Node(value)
        if self.length == 0:
            self.bottom = new_node
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
        return self

    def pop(self):
        "Returns top item and removes it from the stack"
        if self.length == 0:  # or if not self.top
            return None
        if self.length == 1:  # if self.top == self.bottom
            self.bottom = None
        popped = self.top.value  # required if we want to return popped
        self.top = self.top.next
        self.length -= 1
        return popped

    def is_empty(self):
        "Returns true if stack is empty and false otherwise"
        if self.length == 0:
            return True
        else:
            return False

    def traverse(self):  # traversing not encouraged with stacks, O(n)
        values = []
        curr = self.top
        while curr:
            values.append(curr.value)
            curr = curr.next
        return values
"""

stack = Stack()
print(stack.peek())
# print(stack.length)
print(stack.is_empty())
stack.push(1)
# print(stack.length)
print(stack.is_empty())
print(stack.traverse())
print(" ")
print(stack.peek())  # print(stack.peek().value)
# print(stack.top.value)
# print(stack.bottom.value)
print(stack.traverse())
print(" ")
stack.push(2)
# print(stack.length)
print(stack.peek())  # print(stack.peek().value)
# print(stack.top.value)
# print(stack.bottom.value)
print(stack.traverse())
print(" ")
stack.push("google")
# print(stack.length)
print(stack.peek())  # print(stack.peek().value)
# print(stack.top.value)
# print(stack.bottom.value)
print(stack.traverse())
print(" ")
stack.push(3)
# print(stack.length)
print(stack.peek())  # print(stack.peek().value)
# print(stack.top.value)
# print(stack.top.next.value)
# print(stack.bottom.value)
print(stack.traverse())
print(" ")
print(stack.pop())
# print(stack.length)
# print(stack.top.value)
# print(stack.bottom.value)
print(stack.traverse())
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack.traverse())
