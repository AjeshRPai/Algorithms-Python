class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middle_of_linked_list(head):
    current_node = head
    middle_node = head
    counter = 0

    while current_node is not None:
        counter = counter + 1
        if (counter % 2) == 0:
            middle_node = middle_node.next
        current_node = current_node.next

    return middle_node


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
    middle = middle_of_linked_list(node)
    print(middle.value)
