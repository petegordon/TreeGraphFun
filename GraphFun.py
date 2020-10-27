from collections import defaultdict


class Graph:
    def __init__(self):
        self.allNodes = defaultdict(list)
        self.edges = []

    def addEdge(self, node_id_u, node_id_v):
        self.allNodes[node_id_u].append(node_id_v)
        self.edges.append((node_id_u, node_id_v))

    def BreadthSearchFirst(self, node_id_v):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.allNodes))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(node_id_v)
        visited[node_id_v] = True
        result = []
        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")
            result.append(s)

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.allNodes[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        return result


class DAGTree(Graph):
    def __init__(self, rootNode):
        super().__init__()
        self.rootNode = rootNode
        self.allNodes[rootNode.id] = rootNode
        self.allNodes = self.allNodesFlattened(rootNode)

    def allNodesFlattened(self, currentNode):

        for node in currentNode.children:
            self.allNodesFlattened(node)

        self.allNodes[currentNode.id] = currentNode
        return self.allNodes


class GraphNode:
    def __init__(self, id):
        self.id = id
        self.name = "node_"+str(id)
        self.nodeEdges = []


class DAGNode(GraphNode):
    def __init__(self, id):
        super().__init__(id)
        self.children = []
        self.parent = None

    def isChildOf(self, nodeId):
        if(self.parent != None):
            return self.parent.id == nodeId
        return False

    def hasChild(self, nodeId):
        for n in self.children:
            if nodeId == n.id:
                return True
            else:
                return False

    def addChild(self, node):
        if(node not in self.children):
            node.parent = self
            self.children.append(node)

    def findNode(self, findID):
        for child in self.children:
            if(child.id == findID):
                return child

            return child.findNode(self.name)


#edges = [(1, 2), (2, 8), (4, 10), (5, 9), (6, 10), (7, 9)]
edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
nodes = dict()
graph = Graph()
for edge in edges:
    # print(edge)
    graph.addEdge(edge[0], edge[1])
    for n in edge:
        # print(n)
        nodes[n] = n

for count in range(max(nodes.keys())):
    if count not in nodes.keys():
        nodes[count] = -1

print(edges)
print(nodes)
print(graph.allNodes)

print('\n')
result = graph.BreadthSearchFirst(2)
print('\n')
print(result)
