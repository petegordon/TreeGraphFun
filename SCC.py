# Python implementation of Kosaraju's algorithm to print all SCCs

from collections import defaultdict

# This class represents a directed graph using adjacency list representation


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        print(v, end=" ")
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def fillOrder(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    # Function that returns reverse (or transpose) of this graph

    def getTranspose(self):
        g = Graph(self.V)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    # The main function that finds and prints all strongly
    # connected components

    def printSCCs(self):

        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited = [False]*(self.V)
        # Fill vertices in stack according to their finishing
        # times
        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)

        # Create a reversed graph
        gr = self.getTranspose()

        # Mark all the vertices as not visited (For second DFS)
        visited = [False]*(self.V)

        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.DFSUtil(i, visited)
                print("")


# Create a graph given in the above diagram

#edges = [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)]
#edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
g = Graph(len(edges))
for edge in edges:
    g.addEdge(edge[0], edge[1])

print("Following are strongly connected components " +
      "in given graph")
g.printSCCs()
# This code is contributed by Neelam Yadav
