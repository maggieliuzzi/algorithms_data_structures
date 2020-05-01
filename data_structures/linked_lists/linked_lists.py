
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        node = Node(value)
        #next = self.head.next
        ##while next is not None:
        #    next = next.next
        #    next.next = node
        self.tail.next = node
        self.tail = node
        self.length += 1
        return self

    def prepend(self, value):
        node = Node(value, self.head)
        self.head = node
        self.length += 1
        return self

    def traverse_to_index(self, index):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)  # or return -1
        elif index == 0:
            self.prepend(value)
        else:
            leader_node = self.traverse_to_index(index - 1)
            new_node = Node(value, leader_node.next)
            leader_node.next = new_node
        self.length += 1
        return self

    def print_values(self):
        values = []
        current_node = self.head
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next
        return values

linkedList = LinkedList(10)
linkedList.append(5)
linkedList.append(16)

linkedList.append(20)

linkedList.prepend(1)
# print(linkedList.head.value)
# print(linkedList.head.next.value)
# print(linkedList.head.next.next.value)
# print(linkedList.head.next.next.next.value)
# print(linkedList.head.next.next.next.next.value)
# print(linkedList.tail.value)
print(linkedList.print_values())

linkedList.insert(3, 100)
linkedList.insert(2, 200)
linkedList.insert(0, 300)
print(linkedList.insert(10, 1000))
print(linkedList.print_values())
