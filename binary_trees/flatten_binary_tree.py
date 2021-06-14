class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


def flattenBinaryTree(root):
    inOrderNodes = getNodesInOrder(root,[])
    for i in range(0,len(inOrderNodes)-1):
        leftNode = inOrderNodes[i]
        rightNode = inOrderNodes[i+1]
        leftNode.right = rightNode
        rightNode.left = leftNode
    return inOrderNodes[0]

def getNodesInOrder(tree,array,):
    if tree is not None:
        getNodesInOrder(tree.left,array)
        array.append(tree)
        getNodesInOrder(tree.right,array)
    return array


if __name__ == '__main__':
    root = BinaryTree(1).insert([2, 3, 4, 5, 6])
    root.left.right.left = BinaryTree(7)
    root.left.right.right = BinaryTree(8)