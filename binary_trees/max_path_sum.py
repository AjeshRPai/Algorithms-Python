# This is the class of the input binary tree.

# find maximum path in the tree
# path sum is the the sum of the
# values of the nodes in the tree.
# it would be a binary tree so
# will have only left and right nodes

# pseudo code
# find maximum of left and right and then add
# go untill the leaf and return it to the root
# return a left max and right max
# choose left max or right max if its not root
# in case if its root then


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def maxPathSum(tree):
    _, max_sum = find_max_path_sum(tree)
    return max_sum


def find_max_path_sum(tree):
    if tree is None:
        return 0, float("-inf")

    left_max_sum, left_path_sum = find_max_path_sum(tree.left)
    right_max_sum, right_path_sum = find_max_path_sum(tree.right)

    max_child_branch = max(left_max_sum, right_max_sum)
    value = tree.value

    maximum_sum_as_branch = max(max_child_branch + value, value)
    max_sum_as_root_node = max(left_max_sum + value + right_max_sum, maximum_sum_as_branch)

    max_path_sum = max(left_path_sum, right_path_sum, max_sum_as_root_node)

    return maximum_sum_as_branch,max_path_sum


if __name__ == '__main__':
    root = BinaryTree(1)
    root.right = BinaryTree(3)
    root.left = BinaryTree(2)
    root.left.right = BinaryTree(5)
    root.left.left = BinaryTree(4)
    root.left.left.right = BinaryTree(6)
    root.left.left.left = BinaryTree(7)
    print(maxPathSum(root))
