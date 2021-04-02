class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        while self.next is not None:
            self = self.next
            print(self.value)

        if self is None:
            self.value = value

        self.next = LinkedList(value)


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    head_one = linkedListOne
    head_two = linkedListTwo

    while head_one.next is not None and head_two.next is not None:
        print("head one ", head_one.value, "head two ", head_two.value)
        print_linked_list(linkedListOne)
        if head_one.next.value > head_two.value:
            temp_node = head_one.next
            head_one.next = head_two
            head_one.next.next = temp_node
            head_two = head_two.next
        else:
            head_one = head_one.next

    return head_one


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
    list2 = sumOfLinkedLists(node, node6)
    print_linked_list(list2)
