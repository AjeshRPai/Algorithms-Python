from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

            # Step 1: Create a mapping from original nodes to their copies
        old_to_copy = {}

        # First pass: Copy nodes without connecting next and random pointers
        cur = head
        while cur:
            # Copy the current node and store the mapping
            copy_node = Node(cur.val)
            old_to_copy[cur] = copy_node
            cur = cur.next

        # Step 2: Set up next and random pointers in the copied nodes
        cur = head
        while cur:
            copy_node = old_to_copy[cur]
            copy_node.next = old_to_copy.get(cur.next)  # Use .get() to handle None safely
            copy_node.random = old_to_copy.get(cur.random)
            cur = cur.next

        # Return the head of the copied list
        return old_to_copy[head]
