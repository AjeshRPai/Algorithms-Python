class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self,diameter,height):
        self.diameter = diameter
        self.height = height

def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0,0)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPathThroughRoot = leftTreeInfo.height+rightTreeInfo.height
    maxDiameterSoFar = max(leftTreeInfo.diameter,rightTreeInfo.diameter)
    currentDiameter = max(longestPathThroughRoot,maxDiameterSoFar)
    currentHeight = 1+max(leftTreeInfo.height,rightTreeInfo.height)

    return TreeInfo(currentDiameter,currentHeight)


if __name__ == '__main__':
    root = BinaryTree(1)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(7)
    root.right.right = BinaryTree(6)
    root.left = BinaryTree(2)
    root.left.right = BinaryTree(5)
    root.left.left  = BinaryTree(4)
    root.left.left.right = BinaryTree(9)
    root.left.left.left = BinaryTree(8)
    diameter = binaryTreeDiameter(root)
    print(diameter)
