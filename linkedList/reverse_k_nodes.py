from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # Find the kth node
            kth = self.getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next

            # Reverse the group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect the reversed group
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next

    def getKth(self, curr: ListNode, k: int) -> Optional[ListNode]:
        # Find the kth node from the current node
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

def list_to_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_reverse_k_group():
    solution = Solution()

    # Test case 1: Normal case
    head1 = list_to_linked_list([1,2,3,4,5])
    k1 = 2
    print(f"Test 1: head = [1,2,3,4,5], k = {k1}")
    result1 = solution.reverseKGroup(head1, k1)
    print(f"Result: {linked_list_to_list(result1)}")
    print(f"Expected: [2,1,4,3,5]\n")

    # Test case 2: k equals to list length
    head2 = list_to_linked_list([1,2,3,4,5])
    k2 = 5
    print(f"Test 2: head = [1,2,3,4,5], k = {k2}")
    result2 = solution.reverseKGroup(head2, k2)
    print(f"Result: {linked_list_to_list(result2)}")
    print(f"Expected: [5,4,3,2,1]\n")

    # Test case 3: k greater than list length
    head3 = list_to_linked_list([1,2,3,4,5])
    k3 = 6
    print(f"Test 3: head = [1,2,3,4,5], k = {k3}")
    result3 = solution.reverseKGroup(head3, k3)
    print(f"Result: {linked_list_to_list(result3)}")
    print(f"Expected: [1,2,3,4,5]\n")

    # Test case 4: k equals 1 (no reversal)
    head4 = list_to_linked_list([1,2,3,4,5])
    k4 = 1
    print(f"Test 4: head = [1,2,3,4,5], k = {k4}")
    result4 = solution.reverseKGroup(head4, k4)
    print(f"Result: {linked_list_to_list(result4)}")
    print(f"Expected: [1,2,3,4,5]\n")

    # Test case 5: Empty list
    head5 = None
    k5 = 3
    print(f"Test 5: head = [], k = {k5}")
    result5 = solution.reverseKGroup(head5, k5)
    print(f"Result: {linked_list_to_list(result5)}")
    print(f"Expected: []\n")

if __name__ == '__main__':
    test_reverse_k_group()