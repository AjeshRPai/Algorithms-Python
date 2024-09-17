from typing import Optional
# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Create a dummy node pointing to the head
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Step 2: Move the right pointer n steps ahead
        while n > 0:
            right = right.next
            n -= 1

        # Step 3: Move both left and right pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Step 4: Remove the target node
        left.next = left.next.next

        # Return the modified list, skipping the dummy node
        return dummy.next
