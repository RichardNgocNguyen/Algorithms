class Dijkstra:
    def __init__(self):
        self.graph = {}
        self.unvisited = set()
        self.dist = {}
        self.parent = {}
        self.path = []
        self.dequeue = []
    
    def add_edges(self, edge, weight):
        node1, node2 = edge[0], edge[1]
        if node1 not in self.graph:
            self.graph[node1] = {}
            self.unvisited.add(node1)
            self.parent[node1] = None
            self.dist[node1] = 999

        if node1 not in self.graph:
            self.graph[node2] = {}
            self.unvisited.add(node2)
            self.parent[node2] = None
            self.dist[node2] = 999
        
        self.graph[node1][node2] = weight
        
    def dijkstra(self, source):
        root = source
        self.dist[root] = 0
        self.unvisited.remove(root)
        self.dequeue.append(root)
        self.path.append(root)

        while len(self.dequeue) != 0:
            # Traverses through u's nearest neighbors(v) to update the dist table 
            u = self.dequeue.pop(0)
            for v in self.graph[u]:
                weight = self.graph[u][v]
                if self.dist[v] > self.dist[u] + weight:
                    self.dist[v] = self.dist[u] + weight
                    self.parent[v] = u
                    
            # Finds the least costly vertex connection to make
            minimum = 999
            node_ = None
            for vertex in self.dist:
                if self.dist[vertex] < minimum and vertex in self.unvisited:
                    minimum = self.dist[vertex]
                    node_ = vertex

            # Visit and explore the most closest node if it exists
            if node_ is not None:
                self.unvisited.remove(node_)
                self.path.append(node_)
                self.dequeue.append(node_)


G = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

a = Dijkstra()

a.add_edges(('A', 'B'), 4)
a.add_edges(('A', 'H'), 8)

a.add_edges(('B', 'A'), 4)
a.add_edges(('B', 'H'), 11)
a.add_edges(('B', 'C'), 8)

a.add_edges(('C', 'I'), 2)
a.add_edges(('C', 'F'), 4)
a.add_edges(('C', 'D'), 7)
a.add_edges(('C', 'B'), 8)

a.add_edges(('D', 'C'), 7)
a.add_edges(('D', 'F'), 14)
a.add_edges(('D', 'E'), 9)

a.add_edges(('E', 'D'), 9)
a.add_edges(('E', 'F'), 10)

a.add_edges(('F', 'E'), 10)
a.add_edges(('F', 'D'), 14)
a.add_edges(('F', 'C'), 4)
a.add_edges(('F', 'G'), 2)

a.add_edges(('G', 'F'), 2)
a.add_edges(('G', 'I'), 6)
a.add_edges(('G', 'H'), 1)

a.add_edges(('H', 'G'), 1)
a.add_edges(('H', 'I'), 7)
a.add_edges(('H', 'B'), 11)
a.add_edges(('H', 'A'), 8)

a.add_edges(('I', 'H'), 7)
a.add_edges(('I', 'G'), 6)
a.add_edges(('I', 'C'), 2)

a.dijkstra('A')

for i in sorted(a.dist):
    print(f"Distance from A-{i}: ", a.dist[i])

    sequence = [i]
    while sequence[0] != 'A':
        node = sequence[0]
        sequence.insert(0, a.parent[node])
    
    print("Shortest path:", sequence, '\n')

