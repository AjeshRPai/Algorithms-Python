from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function to validate the BST
        def validate(node, low, high):
            # An empty node is valid
            if not node:
                return True

            # The current node's value must be within the range defined by low and high
            if node.val <= low or node.val >= high:
                return False

            # Recursively validate the left and right subtrees
            # The left subtree must be less than the current node's value
            # The right subtree must be greater than the current node's value
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        # Initialize the validation with the full range of possible values
        return validate(root, float('-inf'), float('inf'))