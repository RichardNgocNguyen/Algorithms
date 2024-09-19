import numpy as np


class MST:
    def __init__(self, vertices):
        self.vertices = vertices
        length = len(vertices)
        matrix = (len(vertices), len(vertices))
        # 2D Array
        self.graph = np.full(matrix, 0)
        # BFS based algorithm thus a queue
        self.dequeue = []
        # Returns the order it which it expands to form a minimum spanning tree
        self.path = []
        self.visit = np.full(length, False)
        # Shows minimum cost to connect to a node in a graph
        self.cost = np.full(length, np.NAN)
        # Minimum cost of the tree
        self.total = 0

    def add_edges(self, edge, weight=1):
        # Edge is a set passed in, and we split it to column and row
        columns, rows = edge[0], edge[1]
        # Returns the index coordinates ('A', 'C') --> [0, 2]
        columns, rows = self.convert_coordinates(columns, rows)
        # If edge is not missing any values, we set weights to the edge
        if columns != None and rows != None:
            self.graph[columns][rows] = weight

    # Convert vertex to index
    def to_index(self, vertex):
        for i in range(len(self.vertices)):
            if vertex == self.vertices[i]:
                return i
        return
    
     # Converts index to vertex
    def to_vertex(self, index):
        for i in range(len(self.vertices)):
            if i == index:
                return self.vertices[i]

    # Finds the X and Y of the if the vertices passed in
    def convert_coordinates(self, columns, rows):
        col = row = None
        for y in range(len(self.vertices)):
            if self.vertices[y] == columns:
                col = y
                break
        for x in range(len(self.vertices)):
            if self.vertices[x] == rows:
                row = x
                break
        return col, row

    def minimum_spanning_tree(self, source):
        # Find index of the root
        root_index = self.to_index(source)
        # Set value to 0 as this is the source
        self.cost[root_index] = 0
        # Saves the order of the MST
        self.path.append(source)
        # Mark source as visited
        self.visit[root_index] = True
        # Adds source to the queue to be explored
        self.dequeue.append(source)

        while len(self.dequeue) != 0:
            # Removes the first item in the queue in queue and set to variable u
            u = self.dequeue.pop(0)
            index = self.to_index(u)
            # Return the row associated to variable u
            vertices = self.graph[index]
            # Exploring what variable u is connected to
            for v in range(len(vertices)):
                # Neighbor v is connected but not visited
                if vertices[v] != 0 and self.visit[v] == False:
                    # The value to the vertex is null or new value is less than existing value
                    if np.isnan(self.cost[v]) or vertices[v] <= self.cost[v]:
                        self.cost[v] = vertices[v]

            # Finds the least costly vertex connection to make
            minimum = 1_000_000
            index_value = None
            for i in range(len(self.cost)):
                if self.cost[i] < minimum and self.visit[i] == False:
                    minimum = self.cost[i]
                    index_value = i
            # The next vertex to connect
            self.visit[index_value] = True
            vertex = self.to_vertex(index_value)

            # Index Value is not null when all existing vertexes are not already explored
            if index_value != None:
                # Adds vertex to queue, to order, and add its value to overall cost
                self.dequeue.append(vertex)
                self.path.append(vertex)
                self.total += minimum

    # Return 2D Matrix
    def display(self):
        return self.graph


G = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

for item in G:
    a = MST(G)

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

    a.minimum_spanning_tree(item)
    print(f"MST Source {item}", a.path)
    print("Cost:", a.total, "\n")
    del a
