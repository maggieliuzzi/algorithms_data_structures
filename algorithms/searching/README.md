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
        As deep as possible first
        Space Complexity: O(height of tree)
            The space in memory required is equivalent to the height of the tree, since it will match the deepest recursive function, and that's whats gonna be added to the stack as memory.
            Each function is added to the call stack and starts to return when the end of the tree is reached (no more children/leaf node)
        We typically use recursion
        Lower memory requirement than BFS because it's not necessary to store all the children pointers at each level
        Pros:
            It uses less memory
            Does path exist? (from source node to a target node)
        Cons:
            Can get slow (especially if tree/ graph is really deep, because then we'd have more recursive calls, and therefore also more space complexity, since we need to keep track of those function calls on a stack)
            Not that good at finding shortest path
        Rule of thumb: use if you know the node is likely on lower levels of a tree
        Good for solving a maze. Recursion is good for backtracking and repeating down another path, each step smaller than the other


    - Breadth First Search (BFS)
        Level by level
        Uses additional memory because it tracks all child nodes of all nodes on a given level while searching that level (eg. using a queue or list)
        Pros:
            Shortest path between start/root node and target/reachable node
            Closer nodes. It searches for closer nodes first
        Cons:
            More memory
        Rule of thumb: if additional info on location of node and node is likely in upper levels of a tree
        Good for turning graph into a tree
        Good for finding shortest path between two nodes in a graph and closer nodes


## Searching in graphs
    Note: similar to searching in trees, except that in graphs there is no concept of left or right and there might not be any limit to the number of connections from each node
    Eg. In a recommendation engine, closest items to the one already bought, BFS (shortest path, eg. our closest friends, the most similar book to our favourite one)
    Eg. Type of friend request to recommend, using DFS to check degrees of separation (checking if path exists)


## Shortest path between two vertices in a weighted graph

BFS can do shortest path but it assumes that each path has the same weight, both BFS and DFS disregard the weights of edges (edge is the connection between nodes, which in turn are called vertices)
Eg. some roads are faster than others in Google Maps due to less distance or less traffic

- Bellman-Ford
    Can handle negative weights
    More time complexity
    Worst case: O(n^2)
- Dijkstra
    A little faster and more efficient
    But can't handle negative weights between nodes


## Searching/traversing an array

If sorted:
    Binary Search (divide and conquer): O(log(n)) (eg. by arranging array in a tree-like data structure)
Else:
    Consider sorting (O(n log(n))) and then doing binary search (O(log(n))) (might be faster than doing a Linear Search (O(n)) over and over)

    If sorted won't make it faster:
        Linear Search: O(n)
    If it's a string:
        A Trie data structure might help


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
