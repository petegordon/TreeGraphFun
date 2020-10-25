# Hiearchy and Trees are fun


from pptree import *


class TreeNode:
    def __init__(self, name):
        print("create Node")
        self.name = name
        self.edges = []
        print("Node Name:"+str(name))

    def addEdge(self, edgeNode):
        if(edgeNode not in self.edges):
            self.edges.append(edgeNode)
            strResult = ""
            for n in self.edges:
                strResult += str(n.name) + " "

            print("node:"+str(self.name)+" added edge:" +
                  str(edgeNode.name) + " to edges "+strResult)

    def __str__(self):
        strResult = ""
        for n in self.edges:
            strResult += str(n.name) + " "

        return str(self.name)+"("+strResult+")"


class Tree:
    nodes = []

    def __init__(self, nodeCount, edges):
        print("create Tree")
        print(self.nodes)
        for n in range(10):
            self.nodes.append(TreeNode((n+1)))

        for edge in edges:
            self.createNodesFromEdge(edge)

    def findNode(self, nodeName):
        for n in self.nodes:
            if nodeName == n.name:
                return n

        return None

    def createNodesFromEdge(self, edge):
        nodeLeft = self.findNode(edge[0])
        nodeRight = self.findNode(edge[1])

        nodeLeft.addEdge(nodeRight)
        nodeRight.addEdge(nodeLeft)

    def __str__(self):
        strList = []
        for node in self.nodes:
            strList.append(str(node))
        return str(strList)


count = 10
edges = [(1, 2), (2, 8), (4, 10), (5, 9), (6, 10), (7, 9)]
# edges = [(1, 2)]
tree = Tree(count, edges)
print(tree)

internalNodes = []
rootNode = None
for n in tree.nodes:
    if(len(n.edges) > 1):
        print(">1 degrees: "+str(n.name))
        internalNodes.append(n.name)
    if(len(n.edges) == 0):
        print("zero degrees:"+str(n.name))
        internalNodes.append(n.name)
        if(rootNode == None):
            rootNode = n.name

print(len(internalNodes)-1)
print(internalNodes)
print(rootNode)

newEdges = []
for n in internalNodes:
    if(n != rootNode):
        edge = (rootNode, n)
        newEdges.append(edge)

print(newEdges)
newEdges.extend(edges)
print(newEdges)


class DAGTree:
    def __init__(self, rootNode):
        self.rootNode = rootNode


class DAGNode:
    def __init__(self, id):
        self.id = id
        self.name = "node_"+str(id)
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

    def findNode(findID):
        for child in self.children:
            if(child.id == findID):
                return child

            return child.findNode(name)


allNodeSet = set()
for edge in newEdges:
    allNodeSet.add(edge[0])
    allNodeSet.add(edge[1])

print(allNodeSet)

processed = set()


def checkNewNodeEdgeSide(side, otherSide, currentNode):
    if side == currentNode.id and (currentNode.parent == None or side != currentNode.parent.id):
        if not currentNode.hasChild(otherSide) and not currentNode.isChildOf(otherSide):
            newNode = DAGNode(otherSide)
            currentNode.addChild(newNode)
            return newNode
    return None


def checkNewNode(currentNode, edge):
    left = edge[0]
    right = edge[1]
    if(left == currentNode.id):
        return checkNewNodeEdgeSide(left, right, currentNode)
    if(right == currentNode.id):
        return checkNewNodeEdgeSide(right, left, currentNode)

    return None


def processNode(currentNode, edges):
    if currentNode.name not in processed:
        processed.add(currentNode.name)
        for edge in edges:
            newNode = checkNewNode(currentNode, edge)
            if newNode != None:
                processNode(newNode, edges)

    return currentNode


print(newEdges)
rootNode = DAGNode(3)
print("starting")
rootNode = processNode(rootNode, newEdges)

print("processed::")
print(processed)


def printTree(node):
    strOutput = ""
    if(node.parent != None):
        strOutput = str(node.parent.name)
    else:
        strOutput = "None"
    strOutput += "-"+str(node.name)
    print(strOutput)
    for child in node.children:
        printTree(child)


print("hello world")
printTree(rootNode)

print('\n\n')
print_tree(rootNode, childattr='children', nameattr='name', horizontal=True)
print('\n\n')
