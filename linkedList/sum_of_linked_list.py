class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        while self.next is not None:
            self = self.next
            print(self.value)

        self.next = LinkedList(value)


def get_digit_from_linked_list(head: LinkedList) -> int:
    current = head
    power = 0
    digit = 0
    while current is not None:
        current_digit = current.value * (10 ** power)
        power = power + 1
        digit = digit + current_digit
        current = current.next

    print(digit)
    return digit


def get_digit(number, n):
    return number // 10 ** n % 10


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    first_number = get_digit_from_linked_list(linkedListOne)
    second_number = get_digit_from_linked_list(linkedListTwo)

    sum = second_number + first_number

    digits = []
    for i in range(0, len(str(sum))):
        digits.append(get_digit(sum, i))

    head = LinkedList(digits[0])

    for i in range(1, len(digits)):
        head.add(digits[i])

    return head


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
    node7 = LinkedList(6)
    node6.next = node7
    node8 = LinkedList(7)
    node7.next = node8
    node9 = LinkedList(8)
    node8.next = node9
    node10 = LinkedList(9)
    node9.next = node10
    list2 = sumOfLinkedLists(node, node6)
    print_linked_list(list2)
