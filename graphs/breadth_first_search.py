class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, node):
        self.children.append(node)
        return self

    # time complexity
    # O(V+E)
    # v - vertices
    # e - edges
    # We have to go through every vertices and
    # For every node we add its children nodes
    # to the queue
    def breadthFirstSearch(self, array: []):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array


if __name__ == '__main__':
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")
    nodeG = Node("G")
    nodeH = Node("H")
    nodeI = Node("I")
    nodeJ = Node("J")
    nodeK = Node("K")

    nodeB.addChild(nodeE)
    nodeB.addChild(nodeF)
    nodeF.addChild(nodeI)
    nodeF.addChild(nodeJ)

    nodeA.addChild(nodeB)

    nodeA.addChild(nodeC)

    nodeG.addChild(nodeK)
    nodeD.addChild(nodeG)

    nodeD.addChild(nodeH)

    nodeA.addChild(nodeD)

    array = []
    nodeA.breadthFirstSearch(array)
    for i in array:
        print(i)
