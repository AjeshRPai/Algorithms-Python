from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Initialize an empty stack to store intermediate results

        # Loop through each token in the expression
        for token in tokens:
            if token in {"+", "-", "*", "/"}:  # If the token is an operator
                a = stack.pop()  # Pop the first operand
                b = stack.pop()  # Pop the second operand

                # Perform the operation based on the type of operator
                if token == "+":
                    result = b + a
                elif token == "-":
                    result = b - a
                elif token == "*":
                    result = b * a
                elif token == "/":
                    result = int(float(b) / a)  # Ensure integer division with truncation

                # Push the result back onto the stack
                stack.append(result)
            else:
                # If the token is a number, convert it to an integer and push it onto the stack
                stack.append(int(token))

        # After all tokens are processed, the final result will be the only value left in the stack
        return stack[0]


# Example usage of the intuitive version
if __name__ == "__main__":
    tokens = ["2", "1", "+", "3", "*"]  # Example input
    solution = Solution()
    print(solution.evalRPN(tokens))  # Output: 9
