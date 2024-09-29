class DFS:
    def __init__(self):
        self.graph = {}
        self.color = {}
        self.parent = {}
        self.discovery = {}
        self.finish = {}
        self.time = 0

    def add_edges(self, edge, weight=1):
        node1, node2 = edge[0], edge[1]
        if node1 not in self.graph:
            self.graph[node1] = {}
            self.color[node1] = 'white'
            self.parent[node1] = None
            self.discovery[node1] = 0
            self.finish[node1] = 0
        if node2 not in self.graph:
            self.graph[node2] = {}
            self.color[node2] = 'white'
            self.parent[node2] = None
            self.discovery[node2] = 0
            self.finish[node2] = 0

        self.graph[node1][node2] = weight

    def depth_first_search(self):
        nodes = sorted(set(self.graph)) # Only needed for uniform results
        for n in nodes:
            if self.color[n] == 'white':
                self.dfs_visit(n)

    def dfs_visit(self, u):
        self.color[u] = 'gray'
        self.time += 1
        self.discovery[u] = self.time

        for v in self.graph[u]:
            if self.color[v] == 'white':
                self.parent[v] = u
                self.dfs_visit(v)
        
        self.color[u] = 'black'
        self.time += 1
        self.finish[u] = self.time
            

A = DFS()

A.add_edges(('U', 'V'))
A.add_edges(('U', 'X'))
A.add_edges(('V', 'Y'))
A.add_edges(('W', 'Y'))
A.add_edges(('W', 'Z'))
A.add_edges(('X', 'V'))
A.add_edges(('Y', 'X'))

A.depth_first_search()

print("\nGraph", A.graph, "\n")
print("Nodes", sorted(set(A.graph)), "\n")
# Black is explored, White is not explored
print("Visited", A.color, "\n")
# Time when first discovered
print("Discovered Time:", A.discovery, "\n")
# Time when finished exploring
print("Finished Time", A.finish, "\n")
# Used to find a path to origin node
print("Parent", A.parent)

