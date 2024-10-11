from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Edge case: if prices list is empty or has only one price
        if len(prices) < 2:
            return 0

        # Cache for memoization to store results of states we've already calculated
        cache = {}

        def calculate_profit(day: int, can_buy: bool) -> int:
            """
            Recursive function to calculate maximum profit
            day: current day we're on
            can_buy: boolean indicating if we can buy on this day
            """
            # Base case: if we've gone past the last day
            if day >= len(prices):
                return 0

            # If we've already calculated this state, return cached result
            if (day, can_buy) in cache:
                return cache[(day, can_buy)]

            # Option 1: Skip this day (do nothing)
            do_nothing = calculate_profit(day + 1, can_buy)

            if can_buy:
                # Option 2: Buy stock on this day
                # After buying, we can't buy tomorrow, and we lose money equal to stock price
                buy_stock = calculate_profit(day + 1, False) - prices[day]
                max_profit = max(do_nothing, buy_stock)
            else:
                # Option 3: Sell stock on this day
                # After selling, we need a cooldown day, so we skip to day+2
                # We gain money equal to stock price
                sell_stock = calculate_profit(day + 2, True) + prices[day]
                max_profit = max(do_nothing, sell_stock)

            # Cache the result before returning
            cache[(day, can_buy)] = max_profit
            return max_profit

        # Start from day 0 with ability to buy
        return calculate_profit(0, True)

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit(prices = [1,3,4,0,4]))