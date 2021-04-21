class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_linked_list(headOne, headTwo):
    head_one = headOne
    head_one_prev = None
    head_two = headTwo
    while head_one is not None and head_two is not None:
        if head_one.value < head_two.value:
            head_one_prev = head_one
            head_one = head_one.next
        else:
            if head_one_prev is not None:
                head_one_prev.next = head_two
            head_one_prev = head_two
            head_two = head_two.next
            head_one_prev.next = head_one
    if head_one is None:
        head_one_prev.next = head_two

    return headOne if headOne.value < headTwo.value else headTwo


def print_linked_list(linkedList: LinkedList):
    current_node = linkedList
    list = []
    while current_node.value is not None:
        print(current_node.value)
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
    node3 = LinkedList(3)
    node2.next = node3
    node4 = LinkedList(5)
    node3.next = node4
    node5 = LinkedList(7)
    node4.next = node5

    node6 = LinkedList(2)
    node7 = LinkedList(4)
    node6.next = node7
    node8 = LinkedList(6)
    node7.next = node8
    node9 = LinkedList(8)
    node8.next = node9
    node10 = LinkedList(9)
    node9.next = node10
    print_linked_list(node)
    print_linked_list(node6)
    list2 = merge_linked_list(node, node6)
    print_linked_list(list2)
