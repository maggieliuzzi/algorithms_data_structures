"""
Binary Trees:

Binary Search Trees (BSTs):

    Balanced:
        Lookup: O(log N)
        Insertion: O(log N)
        Deletion: O(log N)

        Number of nodes in tree: 2^height - 1 -> log nodes/number of decisions/steps = height (dropping -1)
            log 100 = 2 because 10^2 = 100
            Divide and conquer

    Unbalanced:
        Lookup: O(n)
        Insertion: O(n)
        Deletion: O(n)

Pros:
If balanced, all operations are better than linear
Ordered
Flexible size (because node can be placed anywhere in memory)
Vs arrays:
    Faster lookups than arrays (O(log N) vs O(n) if unsorted)
    Faster inserts/deletes because of shifting of all indices, unless end (or beginning?)
Vs hash tables:
    Ordered (Python's dicts are ordered now)
    Structure of parent-child relationship
    Slower insertion and search (no O(1), constant time)
On average, an array or a dictionary will have faster operations

Cons:
No O(1) operations, since there often is traversal involved
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value, curr=None):
        ## Recursively
        # if curr == None:
        #     curr = self.root
        # if not curr:
        #     curr = Node(value)
        #     return self
        # if value < curr.value:
        #     curr = curr.left
        # elif value > curr.value:  # in this case, not inserting it at all if value already present
        #     curr = curr.right
        # else:
        #    return -1   # required to avoid infinite loops
        # self.insert(value, curr)

        ## Iteratively
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return self
        curr = self.root
        while True:
            if value < curr.value:
                if not curr.left:
                    curr.left = new_node
                    return self
                curr = curr.left
            elif value > curr.value:
                if not curr.right:
                    curr.right = new_node
                    return self
                curr = curr.right
            else:
                return -1

    def lookup(self, value, curr=None):
        ## Recursive
        # if curr == None:
        #     curr = self.root
        # if not curr:
        #     return None
        # if curr.value == value:
        #     return curr
        # if value < curr.value:
        #     curr = curr.left
        # elif value > curr.value:
        #     curr = curr.right
        # self.lookup(value, curr)

        ## Iterative
        if not self.root:
            return None
        curr = self.root
        while curr:
            if value < curr.value:
                curr = curr.left
            elif value > curr.value:
                curr = curr.right
            elif value == curr.value:
                return curr
        return None  # or False

    def remove(self, value):
        ## Iterative
        if not self.root:
            return -1  # or False
        curr = self.root
        parent = None
        while curr:
            if value < curr.value:
                parent = curr
                curr = curr.left
            elif value > curr.value:
                parent = curr
                curr = curr.right
            elif value == curr.value:
                if not curr.right:  # no right child
                    if not parent:
                        self.root = curr.left
                    else:
                        if curr.value < parent.value:
                            parent.left = curr.left
                        elif curr.value > parent.value:
                            parent.right = curr.left
                elif curr.right and not curr.right.left:  # right child without a left chile
                    if not parent:
                        self.root = curr.left
                    else:
                        curr.right.left = curr.left
                        if curr.value < parent.value:
                            parent.left = curr.right
                        elif curr.value > parent.value:
                            parent.right = curr.right
                elif curr.right and curr.right.left:  # right child with a left child
                    # finding right child's left-most child
                    leftmost = curr.right.left
                    leftmost_parent = curr.right
                    while leftmost.left:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left
                    # parent's left subtree is now leftmost's right subtree
                    leftmost_parent.left = leftmost.right
                    leftmost.left = curr.left
                    leftmost.right = curr.right
                    if not parent:
                        self.root = leftmost
                    else:
                        if curr.value < parent.value:
                            parent.left = leftmost
                        elif curr.value > parent.value:
                            parent.right = leftmost
                return self


    def traverse_BFS(self):  # Iterative
        queue = []  # to keep track of current level  # can use significant memory if its not a binary tree (more than 2 child nodes per parent/ wider tree)
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)  # returns and removes first item in list
            print(node.value, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print("")
    
    def traverse_BFS_recursive(self, queue=None):  # Recursive
        '''
        def traverse_BFS_recursive(self, queue=None):
            if not queue:
                queue = [self.root]
        '''
        if len(queue) == 0:
            print(" ")
            return
        node = queue.pop(0)
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        return self.traverse_BFS_recursive(queue)


    def traverse_DFS_inorder(self, node=None):
        if node == None:
            node = self.root
        if node:
            if node.left:
                self.traverse_DFS_inorder(node.left)
            print(node.value, end=" ")  # left child, parent, right child
            if node.right:
                self.traverse_DFS_inorder(node.right)


    def traverse_DFS_preorder(self, node=None):  # Preorder # Recursive
        if node == None:
            node = self.root
        if node:
            print(node.value, end=" ")  # parent, left child, right child
            if node.left:
                self.traverse_DFS_preorder(node.left)
            if node.right:
                self.traverse_DFS_preorder(node.right)


    def traverse_DFS_postorder(self, node=None):  # Preorder # Recursive
        if node == None:
            node = self.root
        if node:
            if node.left:
                self.traverse_DFS_postorder(node.left)
            if node.right:
                self.traverse_DFS_postorder(node.right)
            print(node.value, end=" ")  # left child, right child, parent


bst = BST()
list = [9, 4, 20, 1, 6, 15, 170]
#       9
#   4      20
# 1   6  15  170
# BFS:                 9 4 20 1 6 15 170
# DFS - in order:      1 4 6 9 15 20 170   sorted
# DFS - pre order:     9 4 1 6 20 15 170   good for recreating a tree
# DFS - post order:    1 6 4 15 170 20 9

for item in list:
    # print(item)
    bst.insert(item)
result_node = bst.lookup(170)
if result_node:
    if result_node.left:
        print(result_node.left.value)
    if result_node.right:
        print(result_node.right.value)
print("\n")
bst.traverse_BFS()
bst.traverse_BFS_recursive([bst.root])  # Can avoid having to pass this argument by creating an intermediary function
bst.traverse_DFS_inorder()
print("")
bst.traverse_DFS_preorder()  # tree = bst.traverse(); print(tree)
print("")
bst.traverse_DFS_postorder()
print("\n\n")
# bst.remove(4)


# Given a binary tree, determine if it is a BST
# i.e. nodes in left subtree are smaller and nodes in right subtree are larger than node
def is_valid_BST(node, lower=float('-inf'), upper=float('inf')):
    if not node:
        return True
    if node.value <= lower or node.value >= upper:
        return False
    return is_valid_BST(node.left, lower, node.value) and is_valid_BST(node.right, node.value, upper)

print(is_valid_BST(bst.root))
