## Key points of the solution:

- The solution uses a binary search approach to find the median of two sorted arrays.
- It ensures the first array is always the shorter one for simplicity.
- The algorithm partitions both arrays and compares elements at the partition points.
- It uses infinity values to handle edge cases when partition points are at array boundaries.
- The time complexity is O(log(min(m,n))), where m and n are the lengths of the input arrays.
- The space complexity is O(1) as it uses only a constant amount of extra space.
