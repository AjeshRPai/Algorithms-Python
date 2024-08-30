from typing import Optional


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize the diameter to 0, which will store the maximum diameter found
        max_diameter = 0

        # Helper function to perform Depth-First Search (DFS) on the tree
        def dfs(node):
            nonlocal max_diameter

            # Base case: if the current node is None, return 0 (height of an empty subtree)
            if not node:
                return 0

            # Recursively find the height of the left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Update the diameter at this node (longest path through the current node)
            max_diameter = max(max_diameter, left_height + right_height)

            # Return the height of the current subtree
            # Height is 1 (for the current node) plus the maximum of the left or right subtree heights
            return 1 + max(left_height, right_height)

        # Start DFS from the root node
        dfs(root)

        # Return the maximum diameter found
        return max_diameter


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.left.left = TreeNode(5)
    diameter = TreeNode(root)
    solution = Solution()
    print(solution.diameterOfBinaryTree(root))