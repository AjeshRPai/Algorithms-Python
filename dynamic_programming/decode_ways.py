class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization dictionary
        memo = {len(s): 1}  # Base case: empty string has 1 way to decode

        def dfs(i):
            # If we've already computed this subproblem, return the result
            if i in memo:
                return memo[i]

            # If current digit is '0', it can't be decoded
            if s[i] == "0":
                return 0

            # Try decoding one digit
            ways = dfs(i + 1)

            # Try decoding two digits if possible
            if i + 1 < len(s) and (
                    s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")
            ):
                ways += dfs(i + 2)

            # Memoize the result
            memo[i] = ways
            return ways

        # Start the recursion from index 0
        return dfs(0)


def test_num_decodings():
    solution = Solution()

    test_cases = [
        ("12", 2),
        ("226", 3),
        ("06", 0),
        ("10", 1),
        ("27", 1),
        ("2101", 1),
        ("123", 3),
        ("", 1),
        ("11106", 2),
        ("1201234", 3)
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.numDecodings(s)
        print(f"Test case {i}:")
        print(f"Input: {s}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print("PASSED" if result == expected else "FAILED")
        print()


if __name__ == "__main__":
    test_num_decodings()
