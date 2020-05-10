"""
Singly linked lists

Can only be traversed forward (i.e. from head to tail)

Comparison with hash tables:
Slow lookups (no random access, traversed is required)
Memory
But:
Ordered (now they are ordered in Python)
Flexible size compared to array, no copying array in memory, with its associated overhead cost and doubling up the space when it reaches its limit - Growing and shrinking as needed
Relatively fast insertion and deletion
Eg. computer file systems, browser history (back and forth), collisions in hash tables (instead of using an array, which is okay for insertion but not for deletion, since it requires unshifting the array, which is slow: O(n))
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def prepend(self, value):  # O(1)
        node = Node(value, self.head)
        self.head = node
        self.length += 1
        return self

    def append(self, value):  # O(1)
        node = Node(value)
        #next = self.head.next
        ##while next is not None:
        #    next = next.next
        #    next.next = node
        self.tail.next = node
        self.tail = node
        self.length += 1
        return self

    def traverse_to_index(self, index):  # O(n). "Lookup". Singly linked lists can only be traversed forward
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node

    def insert(self, index, value):  # O(n)
        if index >= self.length:
            return self.append(value)  # or return -1
        elif index == 0:
            self.prepend(value)
        else:
            leader_node = self.traverse_to_index(index - 1)
            leader_node.next = Node(value, leader_node.next)
        self.length += 1
        return self

    def delete(self, index):  # O(n)
        if index < 0 or index >= self.length:
            return -1
        if index == 0:
            self.head = self.head.next
        else:
            previous = self.traverse_to_index(index - 1)  # also called "leader"
            previous.next = previous.next.next  # unwanted_node = previous.next
        self.length -= 1
        return self

    def print_values(self):  # O(n)
        values = []
        current_node = self.head
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next
        return values

    def reversed(self):
        ## Creating a new LinkedList, not in-place  # O(n^2) memory: O(n) - could be called reversed()
        if self.length == 1:
            return self
        reversed = LinkedList(self.tail.value)
        current = reversed.head.next
        for i in range(3, self.length+1):
            current = self.traverse_to_index(self.length - i)
            reversed.append(current.value)
        return reversed

    def reverse(self, node=None):
        ## Iterative
        '''
        leader = self.head
        self.tail = leader
        follower = leader.next
        while follower:  # for i in range(self.length ..)
            second_next = follower.next
            follower.next = leader
            leader = follower
            follower = second_next
        self.head.next = None
        self.head = leader
        return self
        '''
        '''
        prev = None
        curr = self.head
        next = curr.next
        self.tail = curr

        while curr:  # looping
            # reverse link  # set the next node of current to previous
            curr.next = prev   
            # move to next node  # set previous as current, current as next and next as its next node
            prev = curr  
            curr = next
            if next:
                next = next.next
        self.head = prev  # once curr becomes None, set the head pointer to the previous node
        return self
        '''
        ## Recursive
        if not node.next:
            self.tail = self.head
            self.head = node
            return self
        self.reverse(node.next)
        temp = node.next
        temp.next = node
        node.next = None
        # head.next.next, head.next = head, None

        ''' # Recursive
        if not head or not head.next:
            return head
        rev = self.reverseList(head.next)
        # temp = head.next
        # temp.next = head
        # head.next = None
        head.next.next, head.next = head, None
        return rev
        '''

        '''
        if not head or not head.next:
        return head
        
        ## Recursive
        rev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rev
        
        ## Iterative
        prev = None
        curr = head
        while curr:
            # next = curr.next  # next Node
            # curr.next = prev  # assign prev Node as next
            # prev = curr  # move left
            # curr = next  # move next Node to the back
            curr.next, prev, curr = prev, curr, curr.next
        return prev
        '''
        

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
print(linkedList.insert(15, 1000))
print(linkedList.print_values())

linkedList.delete(1)
print(linkedList.print_values())

linkedList.delete(0)
print(linkedList.print_values())

print(linkedList.delete(15))
print(linkedList.print_values())

print(" ")
reversed_linked_list = linkedList.reversed()
print(reversed_linked_list.print_values())
print(reversed_linked_list.tail.value)

linkedList.reverse(linkedList.head)  # recursive
# linkedList.reverse()  # iterative
print(linkedList.print_values())
print(linkedList.tail.value)
