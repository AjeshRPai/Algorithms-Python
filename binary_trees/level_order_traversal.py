class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def printLevelOrder(root:BinaryTree):
    # Base Case
    if root is None:
        return

    # Create an empty queue
    # for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while (len(queue) > 0):

        # Print front of queue and
        # remove it from queue
        print(queue[0].value)
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

if __name__ == '__main__':
    root = BinaryTree(1)
    root.right = BinaryTree(3)
    root.left = BinaryTree(2)
    root.left.right = BinaryTree(5)
    root.left.left = BinaryTree(4)
    root.left.left.right = BinaryTree(6)
    root.left.left.left = BinaryTree(7)
    print(printLevelOrder(root))