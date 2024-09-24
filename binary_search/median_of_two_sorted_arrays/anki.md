##  Anki card:

Front:
Describe the algorithm to find the median of two sorted arrays with O(log(min(m,n))) time complexity.

Back:
- Use binary search on the shorter array to find the correct partition point.
- Ensure the combined left halves of both arrays have (m+n+1)/2 elements.
- Compare elements at partition points:
  - left1 <= right2 and left2 <= right1 indicates correct partition.
  - If not, adjust the partition in the shorter array.
- Handle edge cases with infinity values for out-of-bounds comparisons.
- For odd total length: median is max(left1, left2).
- For even total length: median is (max(left1, left2) + min(right1, right2)) / 2.
- Time complexity: O(log(min(m,n))), Space complexity: O(1).