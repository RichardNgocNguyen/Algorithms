class BFS:
    def __init__(self):
        self.graph = {}
        self.parent = {}
        self.distance = {}
        self.color = {}
        self.queue = []

    def add_edges(self, edge, weight = 1):
        node1, node2 = edge[0], edge[1]
        if node1 not in self.graph:
            self.graph[node1] = {}
            self.parent[node1] = None
            self.distance[node1] = 0
            self.color[node1] = 'white'
        if node2 not in self.graph:
            self.graph[node2] = {}
            self.parent[node2] = None
            self.distance[node2] = 0
            self.color[node2] = 'white'

        self.graph[node1][node2] = weight

        
    def breadth_first_search(self, root: str):
        self.queue.append(root)
        self.distance[root] = 0
        self.color[root] = 'gray'

        while len(self.queue) != 0:
            u = self.queue.pop(0)
            for v in self.graph[u]:
                if self.color[v] == 'white':
                    self.color[v] = 'gray'
                    self.parent[v] = u
                    weight = self.graph[u][v]
                    self.distance[v] = self.distance[u] + weight
                    self.queue.append(v)
            
            self.color[u] = 'black'
    

A = BFS()

A.add_edges(('U', 'V'))
A.add_edges(('U', 'X'))
A.add_edges(('V', 'Y'))
A.add_edges(('W', 'Y'))
A.add_edges(('W', 'Z'))
A.add_edges(('X', 'V'))
A.add_edges(('Y', 'X'))

A.breadth_first_search('U')

print("\nGraph", A.graph, "\n")
# Listed Nodes
print("Nodes", sorted(set(A.graph)), "\n")
# Black is explored, White is not explored
print("Visited", A.color, "\n")
# Distance to each node from origin node
print("Distance", A.distance, "\n")
# Used to find a path to origin node
print("Parent", A.parent)