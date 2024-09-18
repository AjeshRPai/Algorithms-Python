### 1. Making the Code Intuitive:

- **Sorting**: First, we sort the array to simplify checking for duplicate triplets and enable a two-pointer approach.
- **Outer Loop**: For each number in the sorted array, treat it as the first number (`a`) of a potential triplet.
- **Skip Duplicates**: If the current number is the same as the previous one, skip it to avoid duplicate triplets.
- **Two-pointer Approach**: For each number `a`, use two pointers (`l` and `r`) to find two other numbers that together
  with `a` sum to zero:
    - **Pointer Movement**:
        - If the sum of the triplet is greater than zero, move the right pointer (`r`) to the left to reduce the sum.
        - If the sum is less than zero, move the left pointer (`l`) to the right to increase the sum.
        - If the sum is zero, store the triplet and move both pointers while skipping duplicates to avoid repeated
          results.


### 2. Key Points and Visualization:

#### Key Points:

1. **Sorting**: Sorting the array simplifies the logic for finding unique triplets and helps efficiently apply the
   two-pointer approach.
2. **Two-pointer Technique**:
    - For each number `a`, use two pointers (`l` and `r`) to find the other two numbers such that the sum of the three
      numbers is zero.
    - Adjust the pointers (`l` moves right, `r` moves left) depending on whether the sum is too large or too small.
3. **Avoiding Duplicates**: By skipping over duplicate numbers (both for the outer loop and the two-pointer loop), the
   solution ensures that only unique triplets are added to the result.
4. **Break Early**: If the current number is greater than 0, break the loop, as no valid triplet can have a sum of zero
   when the smallest number is positive.

#### Visualization:

Consider this input array:

```python
nums = [-1, 0, 1, 2, -1, -4]
```

1. **Sorted Array**: `[-4, -1, -1, 0, 1, 2]`
2. **First iteration (`a = -4`)**: Try to find two numbers whose sum equals `4` using two pointers. No such triplet
   exists.
3. **Second iteration (`a = -1`)**: Find the valid triplets `[-1, 0, 1]` and `[-1, -1, 2]`.
4. **Skipping duplicates**: As `a = -1` appears twice consecutively, we skip the second occurrence to avoid repeating
   triplets.

---

