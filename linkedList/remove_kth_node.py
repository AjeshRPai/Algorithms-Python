class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    current_node = head

    node_to_remove = head
    node_before = None
    counter = 0

    while current_node.next is not None:
        counter = counter + 1
        if counter >= k:
            node_before = node_to_remove
            node_to_remove = node_to_remove.next
        current_node = current_node.next


    if counter == k-1:
        head = head.next
        print_linked_list(head)
        return head
    elif counter < k-1:
        print_linked_list(head)
        return head

    node_before.next = node_to_remove.next
    print_linked_list(head)


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
    print_linked_list(node)
    removeKthNodeFromEnd(node, 10)
