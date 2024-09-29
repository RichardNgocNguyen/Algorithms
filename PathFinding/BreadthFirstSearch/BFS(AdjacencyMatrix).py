import numpy as np


class BFS:
    def __init__(self, vertices):
        self.vertices = vertices

        length = len(vertices)
        matrix = (len(vertices), len(vertices))
        self.graph = np.full(matrix, 0) # 2D Array
        self.color = np.full(length, 'white') # Color determines progress
        self.queue = [] # BFS uses a queue data structure

        self.parent = np.full(length, 'None')
        self.distance = np.full(length, 0)

    def add_edges(self, edge, weight=1):
        columns, rows = edge[0], edge[1]
        columns, rows = self.convert_coordinates(columns, rows)
        # Set edge value to the weight
        if columns != None and rows != None:
            self.graph[columns][rows] = weight

    # Convert the vertex to the index
    def to_index(self, vertex: str):
        for i in range(len(self.vertices)):
            if vertex == self.vertices[i]:
                return i

    # Converts index to vertex
    def to_vertex(self, index: int):
        for i in range(len(self.vertices)):
            if i == index:
                return self.vertices[i]

    # Returns the index coordinates ('A', 'B') --> [0, 1]
    def convert_coordinates(self, columns: str, rows: str):
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

    # (u: parent, v: child)
    def breadth_first_search(self, root: str):
        self.queue.append(root)
        while len(self.queue) != 0:
            u = self.queue.pop(0)
            u = self.to_index(u)

            neighbors = self.graph[u]
            for v in range(len(neighbors)):
                if neighbors[v] != 0: # Neighbor does not exist
                    if self.color[v] == 'white': # Unexplored
                        self.color[v] = 'gray'
                        self.parent[v] = self.to_vertex(u)

                        weight = neighbors[v]
                        self.distance[v] = self.distance[u] + weight

                        self.queue.append(self.to_vertex(v))

            # Fully Explored
            self.color[u] = 'black'

    # Displays the matrix
    def display(self):
        return self.graph


nodes = ['U', 'V', 'W', 'X', 'Y', 'Z']
A = BFS(nodes)

A.add_edges(('U', 'V'))
A.add_edges(('U', 'X'))
A.add_edges(('V', 'Y'))
A.add_edges(('W', 'Y'))
A.add_edges(('W', 'Z'))
A.add_edges(('X', 'V'))
A.add_edges(('Y', 'X'))

A.breadth_first_search('U')

print("\n", A.display(), "\n")
# Listed Nodes
print("Nodes", nodes, "\n")
# Black is explored, White is not explored
print("Visited", A.color, "\n")
# Distance to each node from origin node
print("Distance", A.distance, "\n")
# Used to find a path to origin node
print("Parent", A.parent)
