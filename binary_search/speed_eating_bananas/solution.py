from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Start binary search between 1 and the maximum pile size
        l, r = 1, max(piles)
        result = r

        while l <= r:
            # Middle point (possible eating speed)
            k = (l + r) // 2

            # Calculate total time it takes to eat all piles at speed k
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)

            # If the total time is less than or equal to h, we update result and try slower speed
            if totalTime <= h:
                result = k
                r = k - 1  # Try a slower speed (left half)
            else:
                l = k + 1  # Try a faster speed (right half)

        return result


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Koko can finish piles in given time
    piles1 = [3, 6, 7, 11]
    h1 = 8
    print(solution.minEatingSpeed(piles1, h1))  # Expected: 4

    # Test Case 2: Minimum speed to finish in exact hours
    piles2 = [30, 11, 23, 4, 20]
    h2 = 5
    print(solution.minEatingSpeed(piles2, h2))  # Expected: 30

    # Test Case 3: Slower speed, but more hours available
    piles3 = [30, 11, 23, 4, 20]
    h3 = 6
    print(solution.minEatingSpeed(piles3, h3))  # Expected: 23

    # Test Case 4: Single pile with multiple hours
    piles4 = [100]
    h4 = 10
    print(solution.minEatingSpeed(piles4, h4))  # Expected: 10

    # Test Case 5: All piles are small, more than enough hours
    piles5 = [1, 1, 1, 1]
    h5 = 4
    print(solution.minEatingSpeed(piles5, h5))  # Expected: 1
