class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_duplicate_from_linked_list(linkedList: LinkedList):
    current_node = linkedList

    while current_node is not None:
        next_distinct_node = current_node.next
        while next_distinct_node is not None and next_distinct_node.value == current_node.value:
            next_distinct_node = next_distinct_node.next

        current_node.next = next_distinct_node
        current_node = next_distinct_node

    return linkedList


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
    node = LinkedList(1)
    node2 = LinkedList(4)
    node.next = node2
    node3 = LinkedList(5)
    node2.next = node3
    node4 = LinkedList(5)
    node3.next = node4
    node5 = LinkedList(6)
    node4.next = node5
    node6 = LinkedList(6)
    node5.next = node6
    print_linked_list(remove_duplicate_from_linked_list(node))
