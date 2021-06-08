def findLeftSubTree(array):
    root = array[0]
    left_subtree = []
    for index in range(1, len(array)):
        if array[index] < root:
            left_subtree.append(array[index])
    return left_subtree


def findRightSubTree(array):
    root = array[0]
    right_subtree = []
    for index in range(1, len(array)):
        if array[index] >= root:
            right_subtree.append(array[index])
    return right_subtree


def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False

    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    if arrayOne[0] != arrayTwo[0]:
        return False

    left_subtree_1 = findLeftSubTree(arrayOne) if len(arrayOne) != 0 else []
    left_subtree_2 = findLeftSubTree(arrayTwo) if len(arrayTwo) != 0 else []

    print(left_subtree_1)
    print(left_subtree_2)

    left_same = sameBsts(left_subtree_1, left_subtree_2)

    if not left_same:
        return False

    right_subtree_1 = findRightSubTree(arrayOne) if len(arrayOne) != 0 else []
    right_subtree_2 = findRightSubTree(arrayTwo) if len(arrayTwo) != 0 else []
    right_same = sameBsts(right_subtree_1, right_subtree_2)

    return left_same and right_same


if __name__ == '__main__':
    array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
    array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]
    print(sameBsts(array_one, array_two))
