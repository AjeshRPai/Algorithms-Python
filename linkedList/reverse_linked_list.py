class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    head = prev
    return head


# solution 2. By Using recursion
def reverse_linked_list2(head: LinkedList):
    print("head",head.value)
    if head is None or head.next is None:
        return head

    print("head is ",head)
    # Reverse the rest list
    rest = reverse_linked_list2(head.next)

    # Put first element at the end
    head.next.next = head
    head.next = None

    # Fix the header pointer
    return rest


def print_linked_list(linkedList: LinkedList):
    current_node = linkedList

    list = []
    while current_node.value is not None:
        list.append(current_node.value)
        if current_node.next is not None:
            current_node = current_node.next
        else:
            break

    print(list)


if __name__ == '__main__':
    node = LinkedList(0)
    node2 = LinkedList(1)
    node.next = node2
    node3 = LinkedList(2)
    node2.next = node3
    node4 = LinkedList(3)
    node3.next = node4
    node5 = LinkedList(4)
    node4.next = node5
    node6 = LinkedList(5)
    node5.next = node6
    node7 = LinkedList(6)
    node6.next = node7
    node8 = LinkedList(7)
    node7.next = node8
    node9 = LinkedList(8)
    node8.next = node9
    node10 = LinkedList(9)
    node9.next = node10
    # list = reverse_linked_list(node)
    list2 = reverse_linked_list2(node)
    # print_linked_list(list)
    print_linked_list(list2)
