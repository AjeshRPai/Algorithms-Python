# print the lowest sum value which cannot be made using the elements in the array.

# boundary condition
# only positive integers will be given + zero
# if no element present return 0

# pseudocode
# iterate through the coins and check if the value is iterating with a difference of 1

def nonConstructibleChange(coins):
    # Write your code here.
    minimum_value = 0
    if coins:
        coins.sort()
        for coin in coins:
            if coin > minimum_value + 1:
                return minimum_value + 1
            minimum_value += coin
    return minimum_value + 1

if __name__ == '__main__':
    print(nonConstructibleChange([1, 2, 3, 5, 6, 7]))