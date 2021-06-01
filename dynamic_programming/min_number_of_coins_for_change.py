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
    array_of_values = [float('inf')] * (n+1)

    array_of_values[0] = 0

    for coin in denoms:
        for price in range(0, len(array_of_values)):
            print(coin, price)
            if price >= coin:
                array_of_values[price] = min(1 + array_of_values[price - coin], array_of_values[price])

    return array_of_values[n] if array_of_values[n] != float('inf') else -1


if __name__ == '__main__':
    denoms = [1, 5, 10]
    n = 7
    print(minNumberOfCoinsForChange(n, denoms))
