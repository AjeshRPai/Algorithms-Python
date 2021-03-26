class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.id = id


def find_loop(head):
    current_node = head
    visited = {}

    while current_node is not None:
        if current_node in visited:
            return current_node
        visited[current_node] = True
        current_node = current_node.next

    return None


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
    node10.next = node4
    # print_linked_list(node)
    loop = find_loop(node)
    print(loop.value)
    # if loop is not None:
    #     print_linked_list(loop)
