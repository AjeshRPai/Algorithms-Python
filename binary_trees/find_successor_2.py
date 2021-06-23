# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def get_left_most_child(node):
    current_node = node

    while current_node.left is not None:
        current_node = current_node.left

    return current_node


def get_right_most_child(node):
    current_node = node

    while current_node.parent is not None and current_node.parent.right == current_node:
        current_node = current_node.parent

    return current_node.parent

def findSuccessor(tree, node):
    if node.right is not None:
        return get_left_most_child(node.right)

    return get_right_most_child(node)


if __name__ == '__main__':
    root = BinaryTree(1)
    root.right = BinaryTree(3)
    root.right.parent = root
    root.right.left = BinaryTree(7)
    root.right.right = BinaryTree(6)
    root.left = BinaryTree(2)
    root.left.right = BinaryTree(5)
    root.left.left = BinaryTree(4)
    root.left.left.right = BinaryTree(9)
    root.left.left.left = BinaryTree(8)
    successor = findSuccessor(root, root.left.right)
    print(successor.value)
