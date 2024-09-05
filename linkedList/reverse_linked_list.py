from typing import Optional
# Define the ListNode class as per the initial implementation
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev to current
            current = next_node  # Move to the next node
        return prev  # Prev will be the new head after the loop


# Function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()


# Driver code
if __name__ == "__main__":
    # Create a linked list from a list of values
    values = [1, 2, 3, 4, 5]  # Example list
    head = create_linked_list(values)

    print("Original Linked List:")
    print_linked_list(head)

    # Create an instance of Solution and reverse the linked list
    solution = Solution()
    reversed_head = solution.reverseList(head)

    print("Reversed Linked List:")
    print_linked_list(reversed_head)
