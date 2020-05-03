"""
Graphs

Directed or undirected
Weighted or not
Cyclic or acyclic

Pros:
Relationships

Cons:
Scaling is hard. But there are tools such as Neo4j for building fast graph databases
"""

# Edge List  
graph = [[0, 2], [2, 3], [2, 1], [1, 3]]  # weights can be added as a third value, using a dict

# Adjacency List
graph = [[2], [2, 3], [0, 1, 3], [1, 2]]  # could use a dict, especially if keys aren't numbers - weights can be added as a list with each connected value

# Adjacency Matrix  
graph = [
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]                   # weights can be added instead of 0/1s


# Example

# Undirected, unweighted graph using Adjecency List (and a hash table for that)

class Graph:
    def __init__(self):
        self.n_nodes = 0
        self.adjacency_list = {}
    
    def add_vertex(self, node):  # node
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []  # linked lists could be used as well
        self.n_nodes += 1
        return self.adjacency_list

    def add_edge(self, node1, node2):  # connection
        # undirected
        if node1 not in self.adjacency_list or node2 not in self.adjacency_list:
            return -1
        if node2 not in self.adjacency_list[node1]:
            self.adjacency_list[node1].append(node2)
        if node1 not in self.adjacency_list[node2]:
            self.adjacency_list[node2].append(node1)
        return self.adjacency_list

    def show_connections(self):
        for item in self.adjacency_list:
            print(item, " --> ", self.adjacency_list[item])


graph = Graph()
for item in ['0', '1', '2', '3', '4', '5', '6']:
    graph.add_vertex(item)  # shouldn't be called twice in the opposite direction
         
for item in [['3', '1'], ['3', '4'], ['4', '2'], ['4', '5'], ['1', '2'], ['1', '0'], ['0', '2'], ['6', '5'], ['1', '2']]:
    graph.add_edge(item[0], item[1])

graph.add_vertex('4')

graph.show_connections()
