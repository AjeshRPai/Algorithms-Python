from typing import List
from unittest.mock import right


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # This list will store all the valid palindrome partitions
        result = []
        # This list will store the current partition being built
        current_partition = []

        # Helper function to perform depth-first search (DFS)
        def dfs(start_index):
            # If we've reached the end of the string, add the current partition to the result
            if start_index >= len(s):
                result.append(current_partition.copy())
                return

                # Explore all possible partitions starting from the current index
            for end_index in range(start_index, len(s)):
                # If the substring from start_index to end_index is a palindrome
                if self.isPalindrome(s, start_index, end_index):
                    # Add the palindrome substring to the current partition
                    current_partition.append(s[start_index:end_index + 1])
                    # Recursively explore further partitions
                    dfs(end_index + 1)
                    # Backtrack by removing the last added substring
                    current_partition.pop()

        # Start the DFS from the beginning of the string
        dfs(0)

        return result

    # Helper function to check if a substring is a palindrome
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1
        return True

if __name__ == '__main__':
    solution = Solution()
    solution.partition("aab")