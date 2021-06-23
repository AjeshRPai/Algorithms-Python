# conditions
# Non Negative Integer
# Array of positive integers will be the input

# Should return smallest number of coins
# that are needed to make change

# pseudocode
# use dynamic programming
# construct a an array of size denoms*denoms
#

# will the array of denominations sorted ?

def minNumberOfCoinsForChange(n, denoms):
    coins = [float('inf')] * (n + 1)
    coins[0] = 0
    print(coins)

    for value in range(len(coins)):
        for coin in denoms:
            if value >= coin:
                coins[value] = min(1 + coins[value - coin], coins[value])

    return coins[n] if coins[n] != float('inf') else -1


if __name__ == '__main__':
    denoms = [1, 5, 10]
    n = 7
    print(minNumberOfCoinsForChange(n, denoms))
