class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Initialize the result count to 0
        count = 0

        # Helper function to perform depth-first search (DFS)
        def dfs(node, current_max):
            nonlocal count
            if not node:
                return

            # If the current node's value is greater than or equal to the current path maximum, it's a "good" node
            if node.val >= current_max:
                count += 1
                current_max = node.val  # Update the path maximum with the current node's value

            # Continue DFS on the left and right children
            dfs(node.left, current_max)
            dfs(node.right, current_max)

        # Start the DFS from the root with the root's value as the initial maximum
        dfs(root, root.val)
        return count