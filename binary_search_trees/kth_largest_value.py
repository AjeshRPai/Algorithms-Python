# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def printTree(tree):
    print(tree.value)
    if tree.left:
        print('left')
        printTree(tree.left)
    if tree.right:
        print('right')
        printTree(tree.right)


def kthLargestUtil(root, k, c):
    # Base cases, the second condition
    # is important to avoid unnecessary
    # recursive calls
    if root == None or c[0] >= k:
        return

    # Follow reverse inorder traversal
    # so that the largest element is
    # visited first
    kthLargestUtil(root.right, k, c)

    # Increment count of visited nodes
    c[0] += 1

    # If c becomes k now, then this is
    # the k'th largest
    if c[0] == k:
        print("K'th largest element is",
              root.value)
        return

    # Recur for left subtree
    kthLargestUtil(root.left, k, c)


# Function to find k'th largest element
def kthLargest(root, k):
    # Initialize count of nodes
    # visited as 0
    c = [0]

    # Note that c is passed by reference
    kthLargestUtil(root, k, c)


def findKthLargestValue(root, number):
    return kthLargest(root, number)


if __name__ == '__main__':
    root = BinaryTree(1)
    root.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(8)
    root.right.right.right = BinaryTree(9)
    root.right.right.left = BinaryTree(7)
    root.left = BinaryTree(2)
    root.left.right = BinaryTree(3)

    number = 3
    kth_largest = findKthLargestValue(root, number)
    print(kth_largest)
