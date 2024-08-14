from typing import List


def change(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1

    for i in range(len(coins) -1, -1, -1):
        nextDp = [0] * (amount+1)
        nextDp[0] = 1

        for amount in range(1, amount+1):
            nextDp[amount] = dp[amount]
            if amount - coins[i] >=0:
                nextDp[amount] += nextDp[amount-coins[i]]
            print(" ", nextDp[amount], end="")
        dp = nextDp
        print("")
    return dp[amount]


# Time  O(amount)
# Space O(amount)

if __name__ == '__main__':
    print(change(amount=4, coins=[1, 2, 3]))
