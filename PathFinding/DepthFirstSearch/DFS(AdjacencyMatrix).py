import numpy as np

class DFS:
    def __init__(self, vertices):
        self.vertices = vertices

        length = len(vertices)
        matrix = (len(vertices), len(vertices))
        self.graph = np.full(matrix, 0) # Uses 2D Array for graph
        self.color = np.full(length, 'white') # Color determines progress

        self.parent = np.full(length, 'None')
        self.discovery = np.full(length, 0)
        self.finish = np.full(length, 0)
        self.time = 0

    def add_edges(self, edge, weight=1):
        columns, rows = edge[0], edge[1]
        columns, rows = self.convert_coordinates(columns, rows)
        # Set edge value to the weight
        if columns != None and rows != None:
            self.graph[columns][rows] = weight

    # Convert vertex to index
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



    # Loops through each vertex and calls dfs_visit if color is 'white' (unexplored)
    def depth_first_search(self):
        for i in range(len(self.vertices)):
            if self.color[i] == 'white':
                self.dfs_visit(i)

    # Recursively called to traverse the nodes in the graph 
    # (u : parent, v: child)
    def dfs_visit(self, u: int):
        self.color[u] = 'grey' # Exploring
        self.time += 1
        self.discovery[u] = self.time
        
        neighbors = self.graph[u]
        for v in range(len(neighbors)):
            if neighbors[v] != 0 and self.color[v] == 'white': # Is a neighbor and unexplored
                    self.parent[v] = self.to_vertex(u)
                    self.dfs_visit(v)

        # Fully Explored
        self.color[u] = 'black'
        self.time += 1
        self.finish[u] = self.time

    # Displays the 2D Array
    def display(self):
        return self.graph


nodes = ['U', 'V', 'W', 'X', 'Y', 'Z']
A = DFS(nodes)

A.add_edges(('U', 'V'))
A.add_edges(('U', 'X'))
A.add_edges(('V', 'Y'))
A.add_edges(('W', 'Y'))
A.add_edges(('W', 'Z'))
A.add_edges(('X', 'V'))
A.add_edges(('Y', 'X'))

A.depth_first_search()

print("\n", A.display(), "\n")
# Listed Nodes
print("Nodes", nodes, "\n")
# Black is explored, White is not explored
print("Visited", A.color, "\n")
# Time when first discovered
print("Discovered Time:", A.discovery, "\n")
# Time when finished exploring
print("Finished Time", A.finish, "\n")
# Used to find a path to origin node
print("Parent", A.parent)


