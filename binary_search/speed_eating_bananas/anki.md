### Anki Card Based on Key Points

#### Front
How do you use binary search to find the minimum eating speed `k` such that Koko finishes all the piles within `h` hours?

#### Back
1. **Binary Search on Eating Speed**:
   - Search between 1 and the largest pile size. This represents the range of possible eating speeds.

2. **Calculate Total Time for Each Speed**:
   - For each possible speed `k`, calculate how long it takes to eat all piles by summing `math.ceil(p / k)` for each pile.

3. **Adjust Search Range**:
   - If the total time is less than or equal to `h`, reduce the speed (`r = k - 1`).
   - If the time exceeds `h`, increase the speed (`l = k + 1`).

4. **Edge Case**:
   - Consider cases where there's only one pile, or more than enough time (`h` is very large).