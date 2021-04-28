class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, node):
        self.children.append(node)
        return self

    def depthFirstSearch(self, array: []):
        array.append(self.name)
        if self.children is not None:
            for child in self.children:
                child.depthFirstSearch(array)

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
    nodeA.depthFirstSearch(array)
    for i in array:
        print(i)

