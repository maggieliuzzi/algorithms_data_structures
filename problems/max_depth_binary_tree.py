


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value, curr=None):
        if curr == None:
            curr = self.root
        if not curr:
            curr = Node(value)
            return self
        if value < curr.value:
            curr = curr.left
        elif value > curr.value:  # in this case, not inserting it at all if value already present
            curr = curr.right
        else:
           return -1   # required to avoid infinite loops
        self.insert(value, curr)

    def max_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1

    '''
    # Memoised
    def max_depth(self, root):  # TODO (maggie.liuzzi): double check
        """
        :type root: TreeNode
        :rtype: int
        """
        cache = {}
        def memoised(root):
            if not root:
                return 0
            if root in cache:
                return cache[root]
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            cache[root] = max(left_height, right_height) + 1
            return cache[root]
        return memoised
    '''


bst = BST()
for i in [3, 9, 20, None, None, 15, 7]:
    bst.insert(i)  # TOFIX (maggie.liuzzi): self.root is None, so 0 is returned

print(bst.max_depth(bst.root))
