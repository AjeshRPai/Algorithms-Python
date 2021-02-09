# boundary conditions.
# right or left can be null
#

def invertBinaryTree(tree):
    # Write your code here.
    if tree.left:
        invertBinaryTree(tree.left)
    if tree.right:
        invertBinaryTree(tree.right)

    tree.left, tree.right = tree.right, tree.left
    return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def printTree(tree):
    print(tree.value)
    if tree.left:
        print('left')
        printTree(tree.left)
    if tree.right:
        print('right')
        printTree(tree.right)


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
    invertBinaryTree(root)
    printTree(root)

