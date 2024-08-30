from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # To store the right-side view
        q = deque([root])  # Initialize queue with the root node

        while q:
            rightSide = None  # Track the rightmost node at the current level
            qLen = len(q)  # Number of nodes at the current level

            for i in range(qLen):
                node = q.popleft()  # Get the next node
                if node:
                    rightSide = node  # Update the rightmost node
                    q.append(node.left)  # Add left child to queue
                    q.append(node.right)  # Add right child to queue

            if rightSide:
                res.append(rightSide.val)  # Add the rightmost node value to the result

        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    solution = Solution()
    lca = solution.rightSideView(root)
    print(lca)