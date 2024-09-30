class MST:
    def __init__(self):
        self.graph = {}
        self.tree = {} # Node is True if part of minimum spanning tree
        self.cost = {}
        self.total = 0
        self.path = []
        self.dequeue = []
    
    def add_edges(self, edge, weight):
        node1, node2 = edge[0], edge[1]
        if node1 not in self.graph:
            self.graph[node1] = {}
            self.tree[node1] = False
            self.cost[node1] = 999

        if node1 not in self.graph:
            self.graph[node2] = {}
            self.tree[node2] = False
            self.cost[node2] = 999
        
        self.graph[node1][node2] = weight
        
    def minimum_spanning_tree(self, source):
        root = source
        self.cost[root] = 0
        self.tree[root] = True
        self.dequeue.append(root)
        self.path.append(root)

        while len(self.dequeue) != 0:
            # Traverses through u's nearest neighbors(v) to update the cost table 
            u = self.dequeue.pop(0)
            for v in self.graph[u]:
                if self.tree[v] == False:
                    if self.graph[u][v] < self.cost[v]:
                        self.cost[v] = self.graph[u][v]

            # Finds the least costly vertex connection to make
            minimum = 999
            inexpensive_node = None
            for vertex in self.cost:
                if self.cost[vertex] < minimum and self.tree[vertex] == False:
                    minimum = self.cost[vertex]
                    inexpensive_node = vertex

            # Makes a connection with most inexpensive node if it exists
            if inexpensive_node is not None:
                self.tree[inexpensive_node] = True
                self.path.append(inexpensive_node)
                self.dequeue.append(inexpensive_node)
                self.total += minimum

    # Return 2D Matrix
    def display(self):
        return self.graph


G = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

for vertex in G:
    a = MST()

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

    a.minimum_spanning_tree(vertex)
    print(f"MST Source {vertex}", a.path)
    print("Cost:", a.total, "\n")
    del a
