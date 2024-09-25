class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Handle edge case: if either number is 0, return 0
        if "0" in [num1, num2]:
            return "0"

        # Initialize result array with zeros
        # The maximum length of the result will be len(num1) + len(num2)
        res = [0] * (len(num1) + len(num2))

        # Reverse both numbers for easier processing
        num1, num2 = num1[::-1], num2[::-1]

        # Perform multiplication digit by digit
        for i, digit1 in enumerate(num1):
            for j, digit2 in enumerate(num2):
                # Multiply the digits and add to the corresponding position
                product = int(digit1) * int(digit2)
                res[i + j] += product

                # Handle carry
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10

        # Reverse the result and remove leading zeros
        res = res[::-1]
        beg = 0
        while beg < len(res) and res[beg] == 0:
            beg += 1

        # Convert the result to a string
        return "".join(map(str, res[beg:]))

if __name__ == '__main__':
    solution = Solution()

    # Test cases
    test_cases = [
        ("2", "3"),  # Small numbers
        ("123", "456"),  # Medium numbers
        ("9999", "9999"),  # Large numbers
        ("0", "1234"),  # Zero multiplication
        ("1234", "0"),  # Zero multiplication
        ("99999", "99999"),  # Large result
        ("1", "1"),  # Identity
        ("10", "10"),  # Multiples of 10
        ("1000000", "1000"),  # Large number with zeros
        ("1234567890", "9876543210")  # Very large numbers
    ]

    for num1, num2 in test_cases:
        result = solution.multiply(num1, num2)
        expected = str(int(num1) * int(num2))
        print(f"{num1} * {num2}")
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Correct: {result == expected}")
        print("------------------------")

