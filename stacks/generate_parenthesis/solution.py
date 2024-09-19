from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Result list to store all valid combinations
        result = []
        # Stack to help with building the current combination of parentheses
        stack = []

        # Helper function for backtracking
        def backtrack(openCount: int, closeCount: int):
            # If we have added 'n' open and 'n' closed parentheses, the combination is complete
            if openCount == closeCount == n:
                result.append("".join(stack))  # Join the stack to form a valid combination
                return

            # Add an open parenthesis if we haven't reached the limit
            if openCount < n:
                stack.append("(")
                backtrack(openCount + 1, closeCount)
                stack.pop()  # Backtrack: remove the last open parenthesis to explore other paths

            # Add a close parenthesis if it would form a valid sequence
            if closeCount < openCount:
                stack.append(")")
                backtrack(openCount, closeCount + 1)
                stack.pop()  # Backtrack: remove the last close parenthesis

        # Start the backtracking with no open or close parentheses added
        backtrack(0, 0)
        return result


if __name__ == "__main__":
    n = 3  # Example: Generate parentheses for 3 pairs
    solution = Solution()
    result = solution.generateParenthesis(n)
    print(f"Generated Parentheses for n={n}: {result}")

    n = 4  # Another example: Generate parentheses for 4 pairs
    result2 = solution.generateParenthesis(n)
    print(f"Generated Parentheses for n={n}: {result2}")
