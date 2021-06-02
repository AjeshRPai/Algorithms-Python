# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    in_order_traversal = getInOrderTraversal(tree, [])

    print("node ",node)

    for index, current_node in enumerate(in_order_traversal):
        if current_node != node:
            continue

        if index == len(in_order_traversal) - 1:
            return None

        return in_order_traversal[index + 1]


def getInOrderTraversal(tree, array):
    if tree is None:
        return array

    getInOrderTraversal(tree.left, array)

    print(tree.value)
    array.append(tree)

    getInOrderTraversal(tree.right, array)

    return array


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
    diameter = findSuccessor(root, root)
    print(diameter)
