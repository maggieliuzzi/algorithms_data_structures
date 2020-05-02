"""
Double linked lists

Can be traversed forward or backwards (i.e. from tail to head)
Traversing can technically be O(n/2) because we can choose from which end to start. But that's still considered O(n)
For deletion of previous node, no need to traverse from the head node/front
(Insertion and deletion is technically a little faster, because we don't need to move around both next and prev properties, less operations)
Singly linked lists are preferred when memory is a concern, and when you wanna do faster insertion and deletion, and when you don't expect to be doing that much searching (eg. insertion as prepend/append, but not in the middle)
Requires more memory and storage
"""

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def prepend(self, value):  # O(1)
        node = Node(value, self.head)
        self.head.prev = node
        self.head = node
        self.length += 1
        return self

    def append(self, value):  # O(1)
        node = Node(value, prev=self.tail)
        #next = self.head.next
        ##while next is not None:
        #    next = next.next
        #    next.next = node
        self.tail.next = node
        self.tail = node
        self.length += 1
        return self

    def traverse_to_index(self, index, direction=0):  # O(n). "Lookup". Singly linked lists can only be traversed forward
        if direction == 0:  # starting from head
            current_node = self.head
            for i in range(index):  # use while instead?
                current_node = current_node.next
        elif direction == 1:  # starting from tail
            current_node = self.tail
            for i in range(self.length - index - 2):
                current_node = current_node.prev
        return current_node

    def insert(self, index, value):  # O(n)
        if index >= self.length:
            return self.append(value)  # or return -1
        elif index == 0:
            self.prepend(value)
        else:
            leader_node = self.traverse_to_index(index - 1)
            follower_node = leader_node.next
            node = Node(value, prev=leader_node, next=follower_node)
            leader_node.next = node
            follower_node.prev = node
        self.length += 1
        return self

    def delete(self, index):  # O(n)
        if index < 0 or index >= self.length:
            return -1
        if index == 0:
            self.head = self.head.next
        else:
            previous_node = self.traverse_to_index(index - 1)  # also called "leader"
            previous_node.next = previous_node.next.next  # unwanted_node = previous.next
            previous_node.next.prev = previous_node
        self.length -= 1
        return self

    def print_values(self):  # O(n)
        values = []
        current_node = self.head
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next
        return values

linkedList = DoublyLinkedList(10)
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
print(linkedList.insert(15, 1000))
print(linkedList.print_values())

linkedList.delete(1)
print(linkedList.print_values())
linkedList.delete(2)
print(linkedList.print_values())

linkedList.delete(0)
print(linkedList.print_values())

print(linkedList.delete(15))


print(linkedList.head.value)
print(linkedList.head.next.prev.value)
print(linkedList.tail.value)
print(linkedList.tail.prev.next.value)
print(" ")
print(linkedList.traverse_to_index(2).value)
print(linkedList.traverse_to_index(4).value)
print(linkedList.traverse_to_index(4).prev.value)
print(linkedList.traverse_to_index(4).next.value)
print(" ")
print(linkedList.traverse_to_index(2, 1).value)
print(linkedList.traverse_to_index(4, 1).value)
print(linkedList.traverse_to_index(4, 1).prev.value)
print(linkedList.traverse_to_index(4, 1).next.value)
