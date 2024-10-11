from typing import List

class CoinChange:
    def min_coins(self, amount: int, coins: List[int]) -> int:
        # Edge cases
        if amount == 0:
            return 0
        if not coins or amount < 0:
            return -1

        # Initialize dp array with amount + 1 (impossible value)
        # dp[i] represents minimum coins needed for amount i
        min_coins_needed = [amount + 1] * (amount + 1)
        min_coins_needed[0] = 0  # Base case: 0 coins needed for amount 0

        # Build solution bottom-up for each amount
        for current_amount in range(1, amount + 1):
            # Try each coin denomination
            for coin in coins:
                # If we can use this coin (amount - coin >= 0)
                if current_amount >= coin:
                    # Take minimum between:
                    # 1. Current best solution for this amount
                    # 2. 1 coin + solution for (amount - coin)
                    min_coins_needed[current_amount] = min(
                        min_coins_needed[current_amount],
                        1 + min_coins_needed[current_amount - coin]
                    )

        # Return -1 if no solution found, otherwise return minimum coins needed
        return min_coins_needed[amount] if min_coins_needed[amount] != amount + 1 else -1


def run_test_cases():
    """
    Run multiple test scenarios to verify the solution
    """
    solution = CoinChange()

    test_cases = [
        {
            "amount": 11,
            "coins": [1, 2, 5],
            "expected": 3,  # 5 + 5 + 1
            "description": "Basic case with solution"
        },
        {
            "amount": 3,
            "coins": [2],
            "expected": -1,  # Impossible
            "description": "Impossible case"
        },
        {
            "amount": 0,
            "coins": [1, 2, 5],
            "expected": 0,
            "description": "Zero amount"
        },
        {
            "amount": 100,
            "coins": [1, 25, 50],
            "expected": 2,  # 50 + 50
            "description": "Large amount with optimal solution"
        },
        {
            "amount": 6,
            "coins": [3, 4],
            "expected": 2,  # 3 + 3
            "description": "Amount not directly divisible by coins"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.min_coins(test["amount"], test["coins"])
        status = "✓" if result == test["expected"] else "✗"

        print(f"\nTest Case {i}: {test['description']}")
        print(f"Amount: {test['amount']}")
        print(f"Coins: {test['coins']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Status: {status}")


# Run the tests
if __name__ == "__main__":
    run_test_cases()


# Time  O(amount * coins)
# Space O(amount)

