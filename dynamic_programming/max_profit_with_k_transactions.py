def maxProfitWithKTransactions(prices, k):
    if not len(prices):
        return 0
    profits = [[0 for d in prices] for t in range(k + 1)]

    for no_of_xn in range(1, k + 1):
        max_thus_far = float("-inf")
        for cur_price_index in range(1, len(prices)):
            max_thus_far = max(max_thus_far,
                               (profits[no_of_xn - 1][cur_price_index - 1] - prices[cur_price_index - 1]))
            profits[no_of_xn][cur_price_index] = max(profits[no_of_xn][cur_price_index - 1], max_thus_far + prices[cur_price_index])
    return profits[-1][-1]


if __name__ == '__main__':
    prices = [5, 11, 3, 50, 60, 90]
    transaction_allowed = 2
    profit = maxProfitWithKTransactions(prices, transaction_allowed)
    print(profit)
