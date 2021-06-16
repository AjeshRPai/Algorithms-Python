import unittest

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self,root_index):
        self.root_index = root_index


def reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, current_tree):
    if current_tree.root_index == len(preOrderTraversalValues):
        return None

    root_value = preOrderTraversalValues[current_tree.root_index]
    if root_value<lowerBound or root_value>=upperBound:
        return None

    current_tree.root_index+=1
    left = reconstructBstFromRange(lowerBound,root_value,preOrderTraversalValues,current_tree)
    right = reconstructBstFromRange(root_value,upperBound,preOrderTraversalValues, current_tree)
    return BST(root_value,left,right)


def reconstructBst(preOrderTraversalValues):
    tree_info = TreeInfo(0)
    return reconstructBstFromRange(float("-inf"),float("inf"),preOrderTraversalValues,tree_info)



def getDfsOrder(node, values):
    if node is None:
        return
    values.append(node.value)
    getDfsOrder(node.left, values)
    getDfsOrder(node.right, values)
    return values


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        preOrderTraversalValues = [10, 4, 2, 1, 3, 17, 19, 18]
        tree = BST(10)
        tree.left = BST(4)
        tree.left.left = BST(2)
        tree.left.left.left = BST(1)
        tree.left.right = BST(3)
        tree.right = BST(17)
        tree.right.right = BST(19)
        tree.right.right.left = BST(18)
        expected = getDfsOrder(tree, [])
        actual = reconstructBst(preOrderTraversalValues)
        actualDfsOrder = getDfsOrder(actual, [])
        self.assertEqual(actualDfsOrder, expected)


if __name__ == '__main__':
    unittest.main()
