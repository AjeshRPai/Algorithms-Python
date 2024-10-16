from typing import List

# edge cases
# if the amount is less than 0 or the coins array is empty
# if the amount is zero then return 1

# initialize an array that will store the calculation of the min no of coins for that amount
# initialize the amount
# for each coin
#   initialize an 1D array to keep track of the no of ways for each amount
#   assign the  no of ways calculated for that amount till no with the coins so far
#   for each amount check if the amount is greater than the coin in loop,
#  if its greater then check the ways for amount - coin
#   assign the calculated ways to the current ways and return for the target amount
#

def change(targetAmount: int, coins: List[int]) -> int:
    coin_ways = [0] * (targetAmount + 1)
    coin_ways[0] = 1

    for coin in reversed(coins):
        current_ways = [0] * (targetAmount + 1)
        current_ways[0] = 1


        for amount in range(1, targetAmount + 1):
            current_ways[amount] = coin_ways[amount]
            if amount - coin >=0:
                current_ways[amount] += current_ways[amount-coin]

        coin_ways = current_ways
    return coin_ways[targetAmount]


# Time  O(amount)
# Space O(amount)

if __name__ == '__main__':
    print(change(targetAmount=4, coins=[1, 2, 3]))
