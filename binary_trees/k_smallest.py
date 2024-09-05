from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize an empty stack to store nodes during traversal
        stack = []
        current = root

        # Iterate while there are nodes in the stack or the current node is not None
        while stack or current:
            # Traverse to the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Process the node at the top of the stack
            current = stack.pop()
            # Decrement k since we've found one more element in sorted order
            k -= 1

            # If k reaches 0, we've found the k-th smallest element
            if k == 0:
                return current.val

            # Move to the right subtree to continue in-order traversal
            current = current.right
