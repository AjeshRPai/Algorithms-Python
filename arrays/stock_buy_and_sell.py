# https://www.geeksforgeeks.org/stock-buy-sell/
def maxProfit(prices: [int]) -> int:
    i = 0
    n = len(prices)

    profit = 0
    while i < n - 1:
        while i < (n - 1) and (prices[i + 1] <= prices[i]):
            i += 1
        if i == n - 1:
            break

        buy = i
        i += 1

        while i < n and prices[i] >= prices[i - 1]:
            i += 1

        sell = i - 1

        print("Buy on day: ", buy, "\t",
              "Sell on day: ", sell)

        profit += (prices[sell]- prices[buy])

    return profit



if __name__ == '__main__':
    prices = [100, 180, 260, 310, 40, 535, 695]
    profit =  maxProfit(prices)
    print(profit)
