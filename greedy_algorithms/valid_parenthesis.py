def checkValidString(s: str) -> bool:
    min_open, max_open = 0, 0

    for char in s:
        if char == '(':
            min_open += 1
            max_open += 1
        elif char == ')':
            min_open -= 1
            max_open -= 1
        else:
            min_open -= 1
            max_open += 1

        if max_open < 0:
            return False

        if min_open < 0:
            min_open = 0

    return min_open == 0


# Driver Code with Test Cases
if __name__ == "__main__":
    # Test Case 1: Balanced parentheses with *
    s = "(*))"
    print(checkValidString(s))  # Output: True

    # Test Case 2: Too many closing parentheses
    s = "(()"
    print(checkValidString(s))  # Output: False

    # Test Case 3: Balanced parentheses with multiple *
    s = "(*()"
    print(checkValidString(s))  # Output: True

    # Test Case 4: All * which can be balanced
    s = "***"
    print(checkValidString(s))  # Output: True

    # Test Case 5: Unbalanced parentheses without *
    s = "(()))"
    print(checkValidString(s))  # Output: False

    # Test Case 6: All balanced
    s = "()"
    print(checkValidString(s))  # Output: True

    # Test Case 7: Complex combination of parentheses and stars
    s = "(*()*)"
    print(checkValidString(s))  # Output: True

    # Test Case 8: Unbalanced due to excess closing parentheses
    s = "(*)))*("
    print(checkValidString(s))  # Output: False