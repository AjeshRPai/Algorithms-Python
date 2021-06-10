# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findNodesDistanceK(tree, target, k):
    nodesDistancek = []
    findDistanceFromNodeToTarget(tree, target, k, nodesDistancek)
    return nodesDistancek

def findDistanceFromNodeToTarget(node, target, k, nodesDistancek):
    if node is None:
        return -1

    if node.value == target:
        addSubTreeNodesAtDistanceK(node, 0, k, nodesDistancek)
        return 1

    leftDistance = findDistanceFromNodeToTarget(node.left, target, k, nodesDistancek)
    rightDistance = findDistanceFromNodeToTarget(node.right, target, k, nodesDistancek)

    if leftDistance == k or rightDistance == k:
        nodesDistancek.append(node.value)

    if leftDistance != -1:
        addSubTreeNodesAtDistanceK(node.right, leftDistance + 1, k, nodesDistancek)
        return leftDistance + 1

    if rightDistance != -1:
        addSubTreeNodesAtDistanceK(node.right, rightDistance + 1, k, nodesDistancek)
        return rightDistance + 1

    return -1

def addSubTreeNodesAtDistanceK(node, distance, k, nodesDistancek):
    if node is None:
        return

    if distance == k:
        nodesDistancek.append(node.value)
    else:
        addSubTreeNodesAtDistanceK(node.left, distance + 1, k, nodesDistancek)
        addSubTreeNodesAtDistanceK(node.right, distance + 1, k, nodesDistancek)





if __name__ == '__main__':
    root = BinaryTree(1)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(7)
    root.right.right = BinaryTree(6)
    root.left = BinaryTree(2)
    root.left.right = BinaryTree(5)
    root.left.left = BinaryTree(4)
    root.left.left.right = BinaryTree(9)
    root.left.left.left = BinaryTree(8)
    diameter = findNodesDistanceK(root, root)
