# https://www.geeksforgeeks.org/print-left-view-binary-tree/

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def printLeftView(root: BinaryTree):
    # Base Case
    if root is None:
        return

    # Create an empty queue
    # for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while (len(queue) > 0):
        last_element_index = len(queue)

        for i in range(1, last_element_index + 1):
            temp = queue.pop()

            if i == last_element_index:
                print(temp.value)

            if temp.left is not None:
                queue.append(temp.left)

            if temp.right is not None:
                queue.append(temp.right)


if __name__ == '__main__':
    root = BinaryTree(1)
    root.right = BinaryTree(3)
    root.left = BinaryTree(2)
    root.left.right = BinaryTree(5)
    root.left.left = BinaryTree(4)
    root.left.left.right = BinaryTree(6)
    root.left.left.left = BinaryTree(7)
    printLeftView(root)
