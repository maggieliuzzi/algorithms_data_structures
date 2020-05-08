# Searching/ Traversal

- Linear/ Sequential Search
    Finding a target value within a list
    Linear time: O(n)
- Binary Search
    If our data is sorted, we can do better than O(n)
    O(log (n)), since we aren't visiting every item/node, "divide and conquer"
- Traversals
    For both trees and graphs. Eg. looking for a target node, update node somehow
    Time Complexity: O(n)
    - Depth First Search (DFS)
        We typically use recursion
        Lower memory requirement than BFS because it's not necessary to store all the children pointers at each level
        Pros:
            It uses less memory
            Does path exist? (from source node to a target node)
        Cons:
            Can get slow (especially if tree/ graph is really deep)
            Not that good at finding shortest path
        Rule of thumb: use if you know the node is likely on lower levels of a tree
    - Breadth First Search (BFS)
        Uses additional memory because it tracks all child nodes of all nodes on a given level while searching that level
        Pros:
            Shortest path between start/root node and target/reachable node
            Closer nodes. It searches for closer nodes first
        Cons:
            More memory
        Rule of thumb: if additional info on location of node and node is likely in upper levels of a tree


# Real-World Examples

- If you know a solution is not far from the root of the tree:
    BFS, since it starts visiting the closest nodes to the parent first

- If the tree is very deep and solutions are rare: 
    BFS, since DFS would take a long time

- If the tree is very wide:
    Eg. non-binary tree, many child nodes per parent
    DFS, since BFS would require too much memory due to keeping track of all nodes in current level using a queue

- If solutions are frequent but located deep in the tree:
    DFS, since hopefully we should be able to find an answer quicker

- Determining whether a path exists between two nodes:
    DFS

- Finding the shortest path:
    BFS
