class PrefixTreeNode:
    def __init__(self):
        self.children = {}  # Use a dictionary to store child nodes
        self.is_end_of_word = False  # Indicates if the node is the end of a word

class PrefixTree:
    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            # Create a new node if the character is not present in children
            if char not in current_node.children:
                current_node.children[char] = PrefixTreeNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            # If the character is not found, return False
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        # Return True only if current node marks the end of the word
        return current_node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            # If the character is not found, return False
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        # If we can traverse the prefix, it means it exists in the tree
        return True


if __name__ == '__main__':
    # Example usage:
    trie = PrefixTree()
    trie.insert("apple")
    print(trie.search("apple"))  # Returns True
    print(trie.search("app"))    # Returns False
    print(trie.starts_with("app"))  # Returns True
    trie.insert("app")
    print(trie.search("app"))    # Returns True
