class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle base cases
        if n == 0:
            return 1
        if x == 0:
            return 0

        # Handle negative exponents
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            # If n is odd, multiply result by x
            if n % 2 == 1:
                result *= x
            # Square x and halve n in each iteration
            x *= x
            n //= 2

        return result


if __name__ == '__main__':
    solution = Solution()

    # Test cases
    test_cases = [
        (2.0, 10),  # Regular positive exponent
        (2.1, 3),  # Fractional base
        (2.0, -2),  # Negative exponent
        (1.0, 2147483647),  # Large positive exponent
        (-1.0, 2147483647),  # Large positive exponent with negative base
        (2.0, -2147483648),  # Large negative exponent
        (0.0, 5),  # Zero base
        (5.0, 0),  # Zero exponent
        (-2.0, 3),  # Negative base with odd exponent
        (-2.0, 2),  # Negative base with even exponent
    ]

    for x, n in test_cases:
        result = solution.myPow(x, n)
        print(f"x = {x}, n = {n}")
        print(f"myPow(x, n) = {result}")
        print(f"Built-in pow(x, n) = {pow(x, n)}")
        print("------------------------")

