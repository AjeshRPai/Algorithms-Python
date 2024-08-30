from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # to save the computation
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit(prices = [1,3,4,0,4]))