count = 10
edges = [(1, 2), (2, 8), (4, 10), (5, 9), (6, 10), (7, 9)]

allNodes = set()
for n in range(count):
    allNodes.add(n+1)

print(allNodes)
processedTrees = []

# process all edges as nodes and add to treeSet
for edge in edges:
    left = edge[0]
    right = edge[1]

    allNodes.discard(left)
    allNodes.discard(right)
    added = False
    for treeSet in processedTrees:
        if left in treeSet:
            treeSet.add(right)
            added = True
        if right in treeSet:
            treeSet.add(left)
            added = True

    if not added:
        newTreeSet = set()
        newTreeSet.add(left)
        newTreeSet.add(right)
        processedTrees.append(newTreeSet)

print(processedTrees)

# add nodes that have no edges
for noEdge in allNodes:
    noEdgeSet = set()
    noEdgeSet.add(noEdge)
    processedTrees.append(noEdgeSet)

print(processedTrees)
print(len(processedTrees)-1)
