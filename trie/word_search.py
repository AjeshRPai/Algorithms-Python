from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes (key: character, value: TrieNode)
        self.isWord = False  # Flag to mark if this node represents the end of a word
        self.refs = 0  # Reference count to keep track of how many words use this node

    def addWord(self, word):
        cur = self
        cur.refs += 1  # Increment reference count for root node
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()  # Create a new node if character doesn't exist
            cur = cur.children[c]
            cur.refs += 1  # Increment reference count for each character node
        cur.isWord = True  # Mark the end of the word

    def removeWord(self, word):
        cur = self
        cur.refs -= 1  # Decrement reference count for root node
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1  # Decrement reference count for each character node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)  # Build the Trie with all words

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()  # res: set of found words, visit: set of visited cells in current path

        def dfs(r, c, node, word):
            # Check for invalid conditions
            if (r not in range(ROWS) or  # Out of board boundaries
                c not in range(COLS) or  # Out of board boundaries
                board[r][c] not in node.children or  # Character not in Trie
                node.children[board[r][c]].refs < 1 or  # Word already found and removed
                (r, c) in visit):  # Cell already visited in current path
                return

            visit.add((r, c))  # Mark current cell as visited
            node = node.children[board[r][c]]  # Move to the next node in Trie
            word += board[r][c]  # Add current character to the word

            if node.isWord:  # If a word is found
                node.isWord = False  # Mark as not a word to avoid duplicates
                res.add(word)  # Add word to results
                root.removeWord(word)  # Remove word from Trie and update ref counts

            # Recursive DFS in all four directions
            dfs(r + 1, c, node, word)  # Down
            dfs(r - 1, c, node, word)  # Up
            dfs(r, c + 1, node, word)  # Right
            dfs(r, c - 1, node, word)  # Left

            visit.remove((r, c))  # Backtrack: remove current cell from visited set

        # Start DFS from every cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)  # Convert set of found words to list and return

# Example usage:
solution = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(solution.findWords(board, words))