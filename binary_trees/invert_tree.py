# Definition of a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        # Base case: if the root is None, return None
        if not root:
            return None

        # Swap the left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the inverted tree
        return root


# Driver code
def printLevelOrder(root):
    if not root:
        return

    queue = [root]
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            print(node.val, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()  # New line for each level

if __name__ == '__main__':
    # Test cases
    # Case 1: Balanced binary tree
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)

    print("Original Tree 1:")
    printLevelOrder(root1)
    inverted1 = Solution().invertTree(root1)
    print("Inverted Tree 1:")
    printLevelOrder(inverted1)

    # Case 2: Unbalanced binary tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.left.left = TreeNode(4)

    print("\nOriginal Tree 2:")
    printLevelOrder(root2)
    inverted2 = Solution().invertTree(root2)
    print("Inverted Tree 2:")
    printLevelOrder(inverted2)

    # Case 3: Empty tree
    root3 = None
    print("\nOriginal Tree 3:")
    printLevelOrder(root3)
    inverted3 = Solution().invertTree(root3)
    print("Inverted Tree 3:")
    printLevelOrder(inverted3)