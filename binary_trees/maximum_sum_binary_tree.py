# Definition of a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        # Initialize the result with the root value
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Recursively compute the maximum sum for left and right subtrees
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # Ignore negative sums
            left_sum = max(left_sum, 0)
            right_sum = max(right_sum, 0)

            # Compute the maximum path sum through the current node
            path_sum = node.val + left_sum + right_sum

            # Update the global maximum sum if necessary
            self.max_sum = max(self.max_sum, path_sum)

            # Return the maximum sum of a path from this node to one of its children
            return node.val + max(left_sum, right_sum)

        # Start the depth-first search
        dfs(root)

        return self.max_sum


# Driver code
def printTree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            printTree(root.left, level + 1, "L--- ")
            printTree(root.right, level + 1, "R--- ")


if __name__ == '__main__':
    # Test cases
    # Case 1: Balanced binary tree with positive and negative values
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(-6)
    root1.right.right = TreeNode(2)

    print("Tree 1:")
    printTree(root1)
    print("Max Path Sum:", Solution().maxPathSum(root1))
    print()

    # Case 2: Unbalanced binary tree with all negative values except root
    root2 = TreeNode(1)
    root2.left = TreeNode(-2)
    root2.right = TreeNode(-3)
    root2.left.left = TreeNode(-4)
    root2.left.left.left = TreeNode(-5)

    print("Tree 2:")
    printTree(root2)
    print("Max Path Sum:", Solution().maxPathSum(root2))
    print()

    # Case 3: Single node tree
    root3 = TreeNode(-10)

    print("Tree 3:")
    printTree(root3)
    print("Max Path Sum:", Solution().maxPathSum(root3))
    print()

    # Case 4: Tree with a clear maximum path
    root4 = TreeNode(-10)
    root4.left = TreeNode(9)
    root4.right = TreeNode(20)
    root4.right.left = TreeNode(15)
    root4.right.right = TreeNode(7)

    print("Tree 4:")
    printTree(root4)
    print("Max Path Sum:", Solution().maxPathSum(root4))