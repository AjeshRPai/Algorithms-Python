class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        result = []

        def dfs_serialize(node):
            if not node:
                result.append("N")  # N represents null
                return
            result.append(str(node.val))
            dfs_serialize(node.left)
            dfs_serialize(node.right)

        dfs_serialize(root)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        values = data.split(",")
        self.index = 0

        def dfs_deserialize():
            if values[self.index] == "N":
                self.index += 1
                return None
            node = TreeNode(int(values[self.index]))
            self.index += 1
            node.left = dfs_deserialize()
            node.right = dfs_deserialize()
            return node

        return dfs_deserialize()


# Helper function to print the tree
def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")


if __name__ == '__main__':
    # Driver code
    codec = Codec()

    # Test Case 1: Balanced binary tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)

    print("Original Tree 1:")
    print_tree(root1)

    serialized1 = codec.serialize(root1)
    print("Serialized:", serialized1)

    deserialized1 = codec.deserialize(serialized1)
    print("Deserialized Tree 1:")
    print_tree(deserialized1)

    print("\n" + "=" * 50 + "\n")

    # Test Case 2: Unbalanced binary tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.left.left = TreeNode(4)

    print("Original Tree 2:")
    print_tree(root2)

    serialized2 = codec.serialize(root2)
    print("Serialized:", serialized2)

    deserialized2 = codec.deserialize(serialized2)
    print("Deserialized Tree 2:")
    print_tree(deserialized2)

    print("\n" + "=" * 50 + "\n")

    # Test Case 3: Empty tree
    root3 = None

    print("Original Tree 3:")
    print_tree(root3)

    serialized3 = codec.serialize(root3)
    print("Serialized:", serialized3)

    deserialized3 = codec.deserialize(serialized3)
    print("Deserialized Tree 3:")
    print_tree(deserialized3)