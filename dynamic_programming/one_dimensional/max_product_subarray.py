from locale import currency
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
           # storing the value to temp to use the n * curMax value after its recalculated
           temp = curMax * n
           curMax = max(n*curMax,  n*curMin ,n)
           curMin = min(temp, n * curMin, n)
           res = max(res, curMax)

        return res


# Time  O(nums)
# Space O(nums)

if __name__ == '__main__':
    solution = Solution()
    solution.maxProduct(nums = [1,2,-3,4])


