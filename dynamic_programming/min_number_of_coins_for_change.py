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
    change = [float("inf") for amount in range(n + 1)]
    print(len(denoms))
    change[0] = 0
    for coin in denoms:
        for amount in range(len(change)):
            if coin <= amount:
                change[amount] = min(change[amount], 1 + change[amount - coin])

    return change[n] if change[n] != float("inf") else -1


if __name__ == '__main__':
    denoms = [1, 5, 10]
    n = 7
    print(minNumberOfCoinsForChange(n, denoms))
