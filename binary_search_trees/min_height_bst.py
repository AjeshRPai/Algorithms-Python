def minHeightBst(array):
    if len(array) == 1:
        return BST(array[0])

    middle = int(len(array) / 2)
    less = [i for i in array[:middle]]
    greater = [i for i in array[middle + 1:]]


    root = BST(array[middle])

    if less is not None and len(less) != 0:
        root.left = minHeightBst(less)
    if greater is not None and len(greater) != 0:
        root.right = minHeightBst(greater)

    return root

def printTree(tree):
    print(tree.value)
    if tree.left:
        print('left')
        printTree(tree.left)
    if tree.right:
        print('right')
        printTree(tree.right)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


if __name__ == '__main__':
    array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    printTree(minHeightBst(array))
