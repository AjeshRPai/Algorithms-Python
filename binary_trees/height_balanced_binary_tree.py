class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, height, balanced):
        self.height = height
        self.is_balanced = balanced


def heightBalancedBinaryTree(tree):
    # Write your code here.
    return heightBalancedUtil(tree).is_balanced


def heightBalancedUtil(tree) -> TreeInfo:
    if tree is None:
        return TreeInfo(-1, True)

    left_tree_info = heightBalancedUtil(tree.left)
    right_tree_info = heightBalancedUtil(tree.right)

    is_balanced = (left_tree_info.is_balanced \
                   and right_tree_info.is_balanced \
                   and abs(left_tree_info.height
                           - right_tree_info.height) <= 1)

    height = max(left_tree_info.height, right_tree_info.height) + 1

    return TreeInfo(height, is_balanced)


if __name__ == '__main__':
    root = BinaryTree(1)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(7)
    root.right.right = BinaryTree(6)
    root.left = BinaryTree(2)
    root.left.right = BinaryTree(5)
    root.left.left = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    print(heightBalancedBinaryTree(root))
