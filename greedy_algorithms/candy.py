from heaps.last_stone_weight import solution


class Solution:
    def distribute_candies(self, ratings):
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)

if __name__ == '__main__':
    solution = Solution()
    # Test cases
    test_cases = [
        {
            "ratings": [1, 0, 2],
            "expected": 5  # Candies: [2, 1, 2]
        },
        {
            "ratings": [1, 2, 2],
            "expected": 4  # Candies: [1, 2, 1]
        },
        {
            "ratings": [1, 3, 4, 5, 2],
            "expected": 11  # Candies: [1, 2, 3, 4, 1]
        },
        {
            "ratings": [1, 2, 3, 1, 0],
            "expected": 9  # Candies: [1, 2, 3, 2, 1]
        },
        {
            "ratings": [5, 4, 3, 2, 1],
            "expected": 15  # Candies: [5, 4, 3, 2, 1]
        }
    ]

    # Test the function on all test cases
    for i, test_case in enumerate(test_cases):
        ratings = test_case["ratings"]
        expected = test_case["expected"]

        # Call the solution function
        result = solution.distribute_candies(ratings)

        # Compare the result with the expected output
        if result == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed (Expected {expected}, got {result})")


